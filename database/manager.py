from contextlib import contextmanager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
initialized = False


@contextmanager
def get_db_session(commit=True, flush=False):
    yield db.session
    if commit:
        db.session.commit()
    elif flush:
        db.session.flush()


class DatabaseNotInitializedException(Exception):
    pass
