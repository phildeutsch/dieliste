from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
expenses = Table('expenses', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('timestamp', DATETIME),
    Column('user_id', INTEGER),
    Column('description', VARCHAR(length=140)),
    Column('value', FLOAT),
)

expense = Table('expense', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('timestamp', DateTime),
    Column('trip_id', Integer),
    Column('description', String(length=140)),
    Column('value', Float),
)

trip = Table('trip', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('nickname', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=64)),
    Column('email', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['expenses'].drop()
    post_meta.tables['expense'].create()
    post_meta.tables['trip'].create()
    pre_meta.tables['user'].columns['nickname'].drop()
    post_meta.tables['user'].columns['username'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['expenses'].create()
    post_meta.tables['expense'].drop()
    post_meta.tables['trip'].drop()
    pre_meta.tables['user'].columns['nickname'].create()
    post_meta.tables['user'].columns['username'].drop()
