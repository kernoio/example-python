# Kerno
> [!NOTE] **Beta Status**  
> Kerno is still in active development and things may change quickly.  
> We will move out of beta once the core workflow feels smooth for everyday use and we are confident in the developer experience.

Kerno is an integration testing co-pilot for backend developers. It autonomously generates, runs, and maintains context aware tests inside your IDE.


## How to use Kerno extension

Kerno is available on VS Code, Cursor, and Windsurf.

### Getting started
1. Clone this repository
2. Install the Kerno extension from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=kerno.kerno) or from [Open VSX](https://open-vsx.org/extension/Kerno/kerno)
3. Enter your Kerno key when prompted to activate the extension. You can request your key [here](https://www.kerno.io/beta-signup?utm_source=github&utm_medium=pyproject&utm_campaign=early_access
))
4. Kerno will start indexing your codebase automatically. You can track progress in the sidebar.
<img width="706" height="332" alt="Screenshot 2025-11-05 at 15 33 51" src="https://github.com/user-attachments/assets/919ac324-15ed-45a0-aa08-670b8acd3141" />

5. Once indexing is complete, you can begin creating integration tests.

### Creating your first test
1. Open any Python file that contains an endpoint.
<img width="688" height="156" alt="Screenshot 2025-11-05 at 15 37 13" src="https://github.com/user-attachments/assets/6d1e2610-d128-449b-8751-19433bf52a44" />

2. Select the endpoint you want to test.
3. Click the **Run tests with Kerno** button that appears above the function definition.
<img width="1032" height="248" alt="Screenshot 2025-11-05 at 15 27 13" src="https://github.com/user-attachments/assets/b82d0416-6f95-479f-91ef-a2fe246d33ed"/>
4. Kerno will generate and run the tests for you.

# About This Project

This is a complete FastAPI application featuring JWT authentication, user management, and game CRUD operations with PostgreSQL database.

## Features

- 🔐 **Pure JWT Authentication** - Secure login and registration (no OAuth2 dependencies)
- 👤 **User Management** - Full CRUD operations for users
- 🎮 **Game Management** - Full CRUD operations for games
- 🔗 **Relationships** - Users can own multiple games
- 🐘 **PostgreSQL** - Database backend
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

## License
MIT
