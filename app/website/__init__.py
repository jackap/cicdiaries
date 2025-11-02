"""App entrypoint"""

import os
import json
import requests
from flask import Flask, render_template
from flask_cors import CORS
from dotenv import load_dotenv

from .shared.init_setup import setup_logging
from .connection import db
from .models import News
from .routes import blog as blog_route, repos as repos_route
from .admin import setup_admin
import website.utils as utils

load_dotenv()


def create_app(test_config=None):
    """
    Create and configure the Flask app.
    """
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    # Load environment/config
    utils.load_env(test_config, app)

    # Initialize extensions
    db.init_app(app)
    setup_logging(app)
    setup_admin(app)

    # Register blueprints
    register_routes(app)

    # Register core routes
    register_routes_root(app)

    # Ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app


def register_routes(app):
    """Register blueprint routes."""
    app.register_blueprint(repos_route)
    app.register_blueprint(blog_route)


def register_routes_root(app):
    """Register routes for the root and health check."""

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/health")
    def health():
        return "OK"


# CLI commands
def register_cli(app):
    @app.cli.command("createdb")
    def createdb():
        """Create all database tables."""
        print("Creating tables...")
        db.create_all()
        print("Done!")

    @app.cli.command("addrepos")
    def add_repos():
        """Fetch GitHub repos and add them to the database."""
        print("Fetching data from GitHub...")
        r = requests.get(f"https://api.github.com/users/{os.getenv('GITHUB_USER')}/repos")
        json_request = json.loads(r.content)
        for git_repos in json_request:
            if 'name' in git_repos:
                item = News(
                    name=git_repos.get('name'),
                    description=git_repos.get('description'),
                    html_url=git_repos.get('html_url'),
                    date=git_repos.get('created_at'),
                    argument='code'
                )
                if db.session.query(News).filter_by(name=item.name).first():
                    print(f"Value with Name {item.name} exists")
                else:
                    db.session.add(item)
                db.session.flush()
        print("Committing data")
        db.session.commit()


app = create_app()
register_cli(app)
