# FastAPI User & Games API

A complete FastAPI application featuring JWT authentication, user management, and game CRUD operations with PostgreSQL database.

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
│   └── routers/
│       ├── __init__.py
│       ├── auth.py          # Authentication endpoints
│       ├── users.py         # User CRUD endpoints
│       └── games.py         # Game CRUD endpoints
├── requirements.txt
├── docker-compose.yml       # PostgreSQL container
├── env.example              # Environment variables template
└── run.py                   # Development server runner
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

```bash
docker-compose up -d
```

This will start a PostgreSQL container on port 5432.

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


## Development

### Database migrations
```bash
alembic init migrations
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```


# Kerno 

## How to use Kerno extension
1. Install the extension from the marketplace

4. Write the Kerno key to wakeup Kerno

<img src="screenshots/kerno-key.png" alt="Step 1" height="200">

3. Kerno will automatically start indexing the codebase

<img src="screenshots/kerno-indexing.png" alt="Step 1" height="200">

2. When the codebase is indexed you can start creating integration test with Kerno


## License
MIT
