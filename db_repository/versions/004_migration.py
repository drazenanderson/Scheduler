from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
day = Table('day', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('date', DATETIME),
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
)

appointment = Table('appointment', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('client_id', Integer),
    Column('customer_id', Integer),
    Column('schedule_id', Integer),
    Column('address', String(length=120)),
)

window = Table('window', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('date', DateTime),
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
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['day'].drop()
    post_meta.tables['appointment'].create()
    post_meta.tables['window'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['day'].create()
    post_meta.tables['appointment'].drop()
    post_meta.tables['window'].drop()
