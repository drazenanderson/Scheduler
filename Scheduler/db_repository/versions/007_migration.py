from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
client = Table('client', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('user_id', Integer),
)

customer = Table('customer', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['client'].create()
    post_meta.tables['customer'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['client'].drop()
    post_meta.tables['customer'].drop()
