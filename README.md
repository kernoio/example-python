# Kerno
Kerno is an integration testing co-pilot for backend developers. It autonomously generates, runs, and maintains context aware tests inside your IDE.

## How to use Kerno extension

Kerno is available on VS Code, Cursor, and Windsurf.

### Getting started
1. Install the Kerno extension from the VS Code Marketplace. Simply search for Kerno.
2. Enter your Kerno key when prompted to activate the extension.
3. Kerno will start indexing your codebase automatically. You can track progress in the sidebar.
<img width="674" height="453" alt="Screenshot 2025-11-05 at 15 25 31" src="https://github.com/user-attachments/assets/a4ccb5ed-0647-4138-b923-25530fd689c5" />
4. Once indexing is complete, you can begin creating integration tests.

### Creating your first test
1. Open any Python file that contains an endpoint.
2. Select the endpoint you want to test.
3. Click the **Run tests with Kerno** button that appears above the function definition.
<img width="1032" height="248" alt="Screenshot 2025-11-05 at 15 27 13" src="https://github.com/user-attachments/assets/b82d0416-6f95-479f-91ef-a2fe246d33ed" />
4. Kerno will generate and run the tests for you.

# About This Project

This is a complete FastAPI application featuring JWT authentication, user management, and game CRUD operations with PostgreSQL database.

## Features

- 🔐 **Pure JWT Authentication** - Secure login and registration (no OAuth2 dependencies)
- 👤 **User Management** - Full CRUD operations for users
- 🎮 **Game Management** - Full CRUD operations for games
- 🔗 **Relationships** - Users can own multiple games
- 🐘 **PostgreSQL** - Robust database backend
- 📝 **API Documentation** - Auto-generated with Swagger UI and ReDoc
- ✅ **Type Safety** - Pydantic models for request/response validation

## Project Structure

```
example-python/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── database.py          # Database configuration
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── auth.py              # JWT authentication utilities
│   ├── migrations.py        # Migration runner for startup
│   └── routers/
│       ├── __init__.py
│       ├── auth.py          # Authentication endpoints
│       ├── users.py         # User CRUD endpoints
│       └── games.py         # Game CRUD endpoints
├── alembic/
│   ├── env.py               # Alembic environment configuration
│   ├── script.py.mako       # Migration template
│   └── versions/            # Migration scripts directory
│       ├── *.py             # Python migration files
│       ├── *_upgrade.sql    # SQL upgrade scripts
│       └── *_downgrade.sql  # SQL downgrade scripts
├── alembic.ini              # Alembic configuration
├── requirements.txt
├── Dockerfile               # Docker container setup
├── env.example              # Environment variables template
└── README.md                # This file
```

## Prerequisites

- Python 3.8+
- Docker and Docker Compose (for PostgreSQL)
- pip or pipenv

## Installation

### 1. Clone the repository

```bash
cd example-python
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

```bash
cp env.example .env
```

```env
DATABASE_URL=postgresql://user:password@localhost:5432/fastapi_db
SECRET_KEY=your-secret-key-here-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

To generate a secure SECRET_KEY:
```bash
openssl rand -hex 32
```

### 5. Start PostgreSQL database

You'll need a postgres database running.

### 6. Run the application

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## Database Schema

### Users Table
- `id`: Integer (Primary Key)
- `username`: String (Unique)
- `email`: String (Unique)
- `hashed_password`: String
- `created_at`: DateTime

### Games Table
- `id`: Integer (Primary Key)
- `title`: String
- `description`: String (Optional)
- `genre`: String (Optional)
- `owner_id`: Integer (Foreign Key to Users)
- `created_at`: DateTime

**Relationship**: One user can have many games (One-to-Many)


## Database Migrations

This project uses **Alembic** for database migrations with **SQL scripts** that are committed to the repository. Migrations run automatically when the application starts.

### How It Works

1. **Automatic Migration on Startup**: When the application starts, it automatically runs any pending migrations to bring the database schema up to date.

2. **SQL Scripts**: All migrations are defined using raw SQL scripts stored in `alembic/versions/` directory, making the schema changes transparent and version-controlled.

3. **Migration Files**:
   - `c0edcc12896e_initial_migration_with_users_and_games_.py` - Python migration file with SQL operations
   - `c0edcc12896e_initial_migration.sql` - Upgrade SQL script
   - `c0edcc12896e_downgrade.sql` - Downgrade SQL script

### Creating New Migrations

To create a new migration:

```bash
# 1. Create a new migration file
alembic revision -m "Description of migration"

# 2. Edit the generated file in alembic/versions/ and add SQL using op.execute()
# Example:
# def upgrade():
#     op.execute("""
#         ALTER TABLE users ADD COLUMN phone VARCHAR(20)
#     """)

# 3. Generate SQL scripts for documentation
alembic upgrade head --sql > alembic/versions/REVISION_ID_upgrade.sql
alembic downgrade REVISION_ID:base --sql > alembic/versions/REVISION_ID_downgrade.sql

```

### Manual Migration Management

If you need to run migrations manually (without app startup):

```bash
# Upgrade to latest version
alembic upgrade head

# Downgrade one version
alembic downgrade -1

# Show current version
alembic current

# Show migration history
alembic history
```


## License
MIT
