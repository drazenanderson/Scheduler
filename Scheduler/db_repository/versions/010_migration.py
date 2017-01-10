from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
customer = Table('customer', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('user_id', Integer),
    Column('window_id', Integer),
)

client = Table('client', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('user_id', Integer),
    Column('window_id', Integer),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('username', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
    Column('phone', VARCHAR),
    Column('password', VARCHAR(length=64)),
    Column('first', VARCHAR(length=64)),
    Column('last', VARCHAR(length=64)),
    Column('window_id', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['customer'].columns['window_id'].create()
    post_meta.tables['client'].columns['window_id'].create()
    pre_meta.tables['user'].columns['window_id'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['customer'].columns['window_id'].drop()
    post_meta.tables['client'].columns['window_id'].drop()
    pre_meta.tables['user'].columns['window_id'].create()
