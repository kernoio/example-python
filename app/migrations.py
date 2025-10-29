"""
Database migration runner for application startup.
Executes Alembic migrations in offline mode using SQL scripts.
"""
import os
from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine
from app.database import DATABASE_URL
import logging

logger = logging.getLogger(__name__)


def run_migrations():
    """
    Run database migrations on application startup.
    Uses Alembic to apply any pending migrations.
    """
    try:
        # Get the project root directory
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        alembic_ini_path = os.path.join(project_root, "alembic.ini")
        
        # Configure Alembic
        alembic_cfg = Config(alembic_ini_path)
        alembic_cfg.set_main_option("sqlalchemy.url", DATABASE_URL)
        
        logger.info("Running database migrations...")
        
        # Run migrations to the latest version
        command.upgrade(alembic_cfg, "head")
        
        logger.info("Database migrations completed successfully")
        
    except Exception as e:
        logger.error(f"Error running database migrations: {e}")
        raise
