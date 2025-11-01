"""App entrypoint"""

from .shared.init_setup import setup_logging
from .models import News
from .routes import blog as blog_route
from .routes import repos as repos_route
from website.connection import db
from flask_cors import CORS
from flask import Flask,render_template
import json
import os
import requests
import website.utils as utils
from .admin import setup_admin

from dotenv import load_dotenv

load_dotenv()


def create_app(test_config=None):
    """
    Create flask app
    """
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    utils.load_env(test_config, app)
    db.init_app(app)
    setup_logging(app)
    setup_admin(app)
    register_routes(app)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app


def register_routes(app):
    """
    Here I register the routes for the application
    """
    app.register_blueprint(repos_route)
    app.register_blueprint(blog_route)

# ADMIN SETUP


app = create_app()


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/health")
def health():
    """Health check"""
    return 'OK'

# CLI


@app.cli.command('createdb')
def reset_if_needed():
    print('Creating tables.')
    db.create_all()
    print('Shiny!')


@app.cli.command('addrepos')
def add_repos():
    print("Fetching data from github")
    r = requests.get(f"https://api.github.com/users/{os.getenv('GITHUB_USER')}/repos")
    json_request = json.loads(r.content)
    for git_repos in json_request:
        if 'name' in git_repos:
            item = News(name=git_repos['name'],
                        description=git_repos['description'],
                        html_url=git_repos['html_url'],
                        date=git_repos['created_at'],
                        argument='code'
                        )
            if db.session.query(News).filter_by(name=item.name).first():
                print(f'Value with Name {item.name} exists')
            else:
                db.session.add(item)
            db.session.flush()
    print("Committing data")
    db.session.commit()
