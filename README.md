
<p align="center">
<img src="app/website/static/images/whatisthis.png" alt="CI/CD diaries" style="width:40%; height:auto;">
</p>

# CI/CD Diaries

CI/CD Diaries is a simple Portfolio application written with Flask. It is primary designed to experiment with CI/CD pipelines.

The app itself does two main things: 

1. Display GitHub repositories for a given user
2. Manage blog posts

It has an administrative page to manually add, edit and remove posts and repositories.


## Install and run the application

### Prerequisites

You need SQLite installed. Instructions are available [here](https://www.sqlite.org/download.html).

### Environment variables

| Environment Variable             | Description                                              |
| -------------------------------- | -------------------------------------------------------- |
| `SQLALCHEMY_DATABASE_URI`        | The URI for the SQLAlchemy database connection.          |
| `SQLALCHEMY_TRACK_MODIFICATIONS` | Flag to enable/disable SQLAlchemy modification tracking. |
| `SECRET_KEY`                     | Secret key for session management and security needs.    |
| `ADMIN_URL`                      | URL endpoint for the admin interface.                    |
| `ADMIN_USERNAME`                 | Username of the admin user.                              |
| `ADMIN_PASSWORD`                 | Password of the admin user.                              |
| `FLASK_APP`                      | The name of the Flask application.                       |
| `FLASK_ENV`                      | The environment in which the Flask app is running.       |
| `GITHUB_USER`                    | Your GitHub username.                                    |

#### Example `.env`:

```bash
SQLALCHEMY_DATABASE_URI='sqlite:///db/database.db'
SQLALCHEMY_TRACK_MODIFICATIONS=False
SECRET_KEY='dummy_secret'
ADMIN_URL='/admin'
ADMIN_USERNAME='username'
ADMIN_PASSWORD='password'
FLASK_APP='website'
FLASK_ENV='development'
GITHUB_USER='jackap'
SCRIPT_NAME=""
```

> If your app is not hosted at the root, set `SCRIPT_NAME` to the app path.

### Install dependencies

```bash
python3 -m venv venv
pip install -r requirements.txt
pushd app && flask routes && popd # Verify everything works
```

### Run the application locally (testing)

1. Copy environment: `cp .env.dist .env`
2. Go to the app folder: `cd app`
3. Create the database: `flask createdb`
4. Fetch GitHub repository data: `flask addrepos`
5. Run the app: `flask run`

### Unit tests

Run tests using `pytest`.

### Linting

Check code quality with `ruff check app`.

### Source code analysis

Run `bandit app` for security checks.

### Dependency analysis

Audit dependencies using `pip-audit`.

## Production deployment

Use [Gunicorn](https://gunicorn.org/) to deploy the app in production.

Example: `cd app && SCRIPT_NAME="" gunicorn website:app`