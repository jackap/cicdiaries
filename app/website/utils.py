import os


def load_env(test_config=None, app=None):
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.update(
            SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI'),
            SQLALCHEMY_TRACK_MODIFICATIONS=os.environ.get(
                'SQLALCHEMY_TRACK_MODIFICATIONS'),
            SECRET_KEY=os.environ.get('SECRET_KEY'),
            ADMIN_URL=os.environ.get('ADMIN_URL'),
            FLASK_APP=os.environ.get('FLASK_APP'),
            FLASK_ENV=os.environ.get('FLASK_ENV'),
        )
    else:
        # load the test config if passed in
        app.config.update(test_config)
