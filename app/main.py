from fastapi import FastAPI
from app.routers import auth, users, games
from app.migrations import run_migrations

run_migrations()

app = FastAPI(
    title="FastAPI User & Games API",
    description="A FastAPI application with JWT authentication, user management, and game CRUD operations",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(games.router)


@app.get("/")
def root():
    """Root endpoint"""
    return {
        "message": "Welcome to FastAPI User & Games API",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

