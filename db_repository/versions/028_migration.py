from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
customer = Table('customer', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('user_id', INTEGER),
    Column('window_id', INTEGER),
)

window = Table('window', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('date', Date),
    Column('first', Boolean),
    Column('second', Boolean),
    Column('third', Boolean),
    Column('fourth', Boolean),
    Column('fifth', Boolean),
    Column('sixth', Boolean),
    Column('seventh', Boolean),
    Column('eighth', Boolean),
    Column('ninth', Boolean),
    Column('tenth', Boolean),
    Column('eleventh', Boolean),
    Column('twelfth', Boolean),
    Column('thirteenth', Boolean),
    Column('fourteenth', Boolean),
    Column('fifteenth', Boolean),
    Column('sixteenth', Boolean),
    Column('customer_id', Integer),
    Column('client_id', Integer),
    Column('user_id', Integer),
)

client = Table('client', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('user_id', INTEGER),
    Column('window_id', INTEGER),
)

appointment = Table('appointment', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('client_id', Integer),
    Column('customer_id', Integer),
    Column('schedule_id', Integer),
    Column('address', String(length=120)),
    Column('confirmed', Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['customer'].columns['window_id'].drop()
    post_meta.tables['window'].columns['client_id'].create()
    post_meta.tables['window'].columns['customer_id'].create()
    pre_meta.tables['client'].columns['window_id'].drop()
    post_meta.tables['appointment'].columns['confirmed'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['customer'].columns['window_id'].create()
    post_meta.tables['window'].columns['client_id'].drop()
    post_meta.tables['window'].columns['customer_id'].drop()
    pre_meta.tables['client'].columns['window_id'].create()
    post_meta.tables['appointment'].columns['confirmed'].drop()
