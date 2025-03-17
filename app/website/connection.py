from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Query 
db = SQLAlchemy(session_options={
    'autoflush': False, 'query_cls': Query})
