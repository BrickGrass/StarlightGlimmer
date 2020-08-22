from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from objects.database_models.animote_user import AnimoteUser
from objects.database_models.guild import Guild
from objects.database_models.menu_lock import MenuLock
from objects.database_models.muted_template import MutedTemplate
from objects.database_models.snapshot import Snapshot
from objects.database_models.template import Template
from objects.database_models.version import Version

from utils import config

engine = create_engine(config.DATABASE_URI)
session_factory = sessionmaker(bind=engine, expire_on_commit=False)
Session = scoped_session(session_factory)

Base.metadata.create_all(engine)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    finally:
        session.close()
