import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Entry(Base):
    __tablename__ = 'entries'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.Unicode(255), unique=True, nullable=False)
    body = sa.Column(sa.UnicodeText)
    created = sa.Column(sa.DateTime, default=sa.func.now())
    edited = sa.Column(sa.DateTime, default=sa.func.now(), onupdate=sa.func.now())

    @classmethod
    def all(cls):
        return session.query.order_by(Session.DateTime).all()

    @classmethod
    def by_id(cls, id):
        return session.query(Entry).filter(Entry.id==id).first()
        

sa.Index('my_index', Entry.title, unique=True, mysql_length=255)
