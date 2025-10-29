"""Initial migration with users and games tables

Revision ID: c0edcc12896e
Revises: 
Create Date: 2025-10-29 10:05:40.505153

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c0edcc12896e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create users table
    op.execute("""
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username VARCHAR NOT NULL UNIQUE,
            email VARCHAR NOT NULL UNIQUE,
            hashed_password VARCHAR NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Create indexes on users table
    op.execute("CREATE INDEX ix_users_username ON users(username)")
    op.execute("CREATE INDEX ix_users_email ON users(email)")
    op.execute("CREATE INDEX ix_users_id ON users(id)")
    
    # Create games table
    op.execute("""
        CREATE TABLE games (
            id SERIAL PRIMARY KEY,
            title VARCHAR NOT NULL,
            description VARCHAR,
            genre VARCHAR,
            owner_id INTEGER NOT NULL REFERENCES users(id),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Create indexes on games table
    op.execute("CREATE INDEX ix_games_title ON games(title)")
    op.execute("CREATE INDEX ix_games_id ON games(id)")


def downgrade() -> None:
    # Drop tables in reverse order
    op.execute("DROP TABLE IF EXISTS games")
    op.execute("DROP TABLE IF EXISTS users")
