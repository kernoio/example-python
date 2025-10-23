# Quick Start Guide

Get your FastAPI User & Games API running in 5 minutes!

## Method 1: Automated Setup (Recommended for Unix/Mac)

```bash
# Make setup script executable
chmod +x setup.sh

# Run setup
./setup.sh

# Generate a secure secret key
openssl rand -hex 32

# Update the SECRET_KEY in .env with the generated key

# Activate virtual environment
source venv/bin/activate

# Run the application
python run.py
```

## Method 2: Manual Setup

```bash
# 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up environment
cp env.example .env
# Edit .env and update SECRET_KEY

# 4. Start PostgreSQL
docker-compose up -d

# 5. Run the application
python run.py
```

## Verify Installation

Open your browser and visit:
- **API Root**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

## First Steps

### 1. Register a User
Go to http://localhost:8000/docs and try the `/auth/register` endpoint:

```json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "password123"
}
```

### 2. Login
Use the `/auth/login` endpoint with your credentials to get a token.

### 3. Authorize
Click the "Authorize" button in Swagger UI and enter: `Bearer YOUR_TOKEN`

### 4. Create a Game
Try the `/games/` POST endpoint:

```json
{
  "title": "My Awesome Game",
  "description": "A fun game",
  "genre": "Action"
}
```

### 5. View Your Games
Use the `/users/me/games` GET endpoint to see all your games!

## Troubleshooting

### Port 5432 Already in Use
If PostgreSQL port is already taken:
```bash
# Stop the container
docker-compose down

# Change the port in docker-compose.yml (e.g., "5433:5432")
# Update DATABASE_URL in .env accordingly
```

### ModuleNotFoundError
Make sure your virtual environment is activated:
```bash
source venv/bin/activate  # Unix/Mac
venv\Scripts\activate     # Windows
```

### Database Connection Error
Verify PostgreSQL is running:
```bash
docker-compose ps
```

If not running:
```bash
docker-compose up -d
```

## Next Steps

- Read [API_EXAMPLES.md](API_EXAMPLES.md) for detailed API usage examples
- Check out [README.md](README.md) for comprehensive documentation
- Explore the interactive API docs at http://localhost:8000/docs

## Stopping the Application

```bash
# Stop the FastAPI server
Ctrl+C

# Stop PostgreSQL
docker-compose down

# Deactivate virtual environment
deactivate
```

## Need Help?

Check the comprehensive documentation in README.md or explore the API interactively at http://localhost:8000/docs

