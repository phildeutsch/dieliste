from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
trips = Table('trips', post_meta,
    Column('trip_id', Integer),
    Column('user_id', Integer),
)

trip = Table('trip', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('start_date', DateTime),
    Column('end_date', DateTime),
    Column('destination', String(length=128)),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['trips'].create()
    post_meta.tables['trip'].columns['destination'].create()
    post_meta.tables['trip'].columns['end_date'].create()
    post_meta.tables['trip'].columns['start_date'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['trips'].drop()
    post_meta.tables['trip'].columns['destination'].drop()
    post_meta.tables['trip'].columns['end_date'].drop()
    post_meta.tables['trip'].columns['start_date'].drop()
