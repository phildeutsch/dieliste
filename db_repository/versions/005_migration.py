from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
expense = Table('expense', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('user_id', Integer),
    Column('timestamp', DateTime),
    Column('trip_id', Integer),
    Column('description', String(length=140)),
    Column('value', Float),
)

trip = Table('trip', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['expense'].columns['user_id'].create()
    post_meta.tables['trip'].columns['user_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['expense'].columns['user_id'].drop()
    post_meta.tables['trip'].columns['user_id'].drop()
