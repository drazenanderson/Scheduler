from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
window = Table('window', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('date', DATE),
    Column('first', BOOLEAN),
    Column('second', BOOLEAN),
    Column('third', BOOLEAN),
    Column('fourth', BOOLEAN),
    Column('fifth', BOOLEAN),
    Column('sixth', BOOLEAN),
    Column('seventh', BOOLEAN),
    Column('eighth', BOOLEAN),
    Column('ninth', BOOLEAN),
    Column('tenth', BOOLEAN),
    Column('eleventh', BOOLEAN),
    Column('twelfth', BOOLEAN),
    Column('thirteenth', BOOLEAN),
    Column('fourteenth', BOOLEAN),
    Column('fifteenth', BOOLEAN),
    Column('sixteenth', BOOLEAN),
    Column('user_id', INTEGER),
    Column('client_id', INTEGER),
    Column('customer_id', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['window'].columns['user_id'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['window'].columns['user_id'].create()
