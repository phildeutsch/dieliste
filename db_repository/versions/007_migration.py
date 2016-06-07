from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
trips = Table('trips', pre_meta,
    Column('trip_id', INTEGER),
    Column('user_id', INTEGER),
)

association = Table('association', post_meta,
    Column('user_id', Integer),
    Column('trip_id', Integer),
    Column('expense_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['trips'].drop()
    post_meta.tables['association'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['trips'].create()
    post_meta.tables['association'].drop()
