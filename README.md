# CI/CD Diaries 

CI/CD Diaries is a very simple Flask application that displays the Github repositories of a given user. It is intended to experiment with CI/CD pipelines.

![What is this?](app/website/static/images/whatisthis.webp)
> Note: The image above is AI-generated.

## Install and run the application

### Environment variables:


| Environment Variable         | Description                                                   |
|------------------------------|---------------------------------------------------------------|
| `SQLALCHEMY_DATABASE_URI`    | The URI for the SQLAlchemy database connection.               |
| `SQLALCHEMY_TRACK_MODIFICATIONS` | Flag to enable/disable SQLAlchemy modification tracking.  |
| `SECRET_KEY`           | Secret key for session management and other security-related needs. |
| `ADMIN_URL`                  | URL endpoint for the admin interface.                         |
| `FLASK_APP`                  | The name of the Flask application.                            |
| `FLASK_ENV`                  | The environment in which the Flask app is running.            |
| `GITHUB_USER`                | Your Github username                                          |

#### Example: 

```bash
SQLALCHEMY_DATABASE_URI = 'sqlite:///db/database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dummy_secret"
ADMIN_URL = "/admin"
ADMIN_PASSWORD = "password"
ADMIN_USERNAME = "username"
FLASK_APP = 'website'
FLASK_ENV = 'development'
GITHUB_USER = 'jackap'
```

> If you do not host the app at the root of the domain (e.g., your app is available at 10.10.10.10/test instead of 10.10.10.10) then you need to specify  the `SCRIPT_NAME` environment variable with the app path (test in the example).

### Install dependencies

1. `pip install -r requirements.txt`
2. Verify installation: `cd app && flask routes` (should show the different routes of the server)

### Unit tests

We use `pytest` for unit tests in this app.

### Linting

This application uses `pylint` for linting code.

### Source code analysis

We use `bandit` for source code analysis.

### Dependency analysis

`pip-audit` is the tool we use for auditing the dependencies.


## Production deployment

Use [gunicorn](https://gunicorn.org/) to deploy the app in production.