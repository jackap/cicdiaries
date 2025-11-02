from flask import request, render_template, redirect, url_for

from flask_admin import Admin
from website.models import News, BlogPost
from website.connection import db
from flask_login import LoginManager, login_user, logout_user
import os
from .admin_views import NewsView, BlogView, User, MyAdminIndexView
from .simplemde import SimpleMDE

def setup_admin(app):
    SimpleMDE(app)
    admin = Admin(app, 'Blog Admin',
                  template_mode='bootstrap3',
                          index_view=MyAdminIndexView(url=os.environ.get('ADMIN_URL')))
    admin.add_view(NewsView(News, db.session, endpoint='_news'))
    admin.add_view(BlogView(BlogPost, db.session, endpoint='_blog'))

    login_manager = LoginManager()
    login_manager.init_app(app)
    # callback to reload the user object
    @login_manager.user_loader
    def load_user(userid):
        return User(userid)

    @app.route("/login", methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            # handle hardcoded user login
            username = request.form['username']
            password = request.form['password']
            if (username == os.environ.get('ADMIN_USERNAME')
                    and password == os.environ.get('ADMIN_PASSWORD')):
                login_user(User(username))
                return  redirect(url_for('admin.index'))

        return render_template('login.html', error=True)

    @app.route("/logout")
    def logout():
        logout_user()
        app.logger.info('Logged out')
        return redirect(url_for('home'))
