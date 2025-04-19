from logging.config import fileConfig
import os, sys
from alembic import context
from sqlalchemy import engine_from_config, pool

config = context.config

# Use the correct path for alembic.ini (project root)
alembic_ini_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'alembic.ini'))
if os.path.exists(alembic_ini_path):
    fileConfig(alembic_ini_path)

# Add your app to the path so we can import db metadata
sys.path.append(os.getcwd())
from app import app, db

target_metadata = db.metadata

def run_migrations_offline():
    url = app.config['SQLALCHEMY_DATABASE_URI']
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    # Inject the Flask app's DB URI into Alembic config
    config.set_main_option('sqlalchemy.url', app.config['SQLALCHEMY_DATABASE_URI'])
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
