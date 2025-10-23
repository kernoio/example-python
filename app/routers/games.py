from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import schemas, models
from app.database import get_db
from app.auth import get_current_user

router = APIRouter(prefix="/games", tags=["games"])

@router.post("/", response_model=schemas.GameResponse, status_code=status.HTTP_201_CREATED)
def create_game(
    game: schemas.GameCreate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new game for the current user"""
    db_game = models.Game(
        **game.model_dump(),
        owner_id=current_user.id
    )
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


@router.get("/", response_model=List[schemas.GameResponse])
def read_games(
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all games"""
    games = db.query(models.Game).offset(skip).limit(limit).all()
    return games


@router.get("/user/{user_id}", response_model=List[schemas.GameResponse])
def read_games_by_user(
    user_id: int,
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all games from a specific user"""

    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    games = db.query(models.Game).filter(
        models.Game.owner_id == user_id
    ).offset(skip).limit(limit).all()
    return games


@router.get("/{game_id}", response_model=schemas.GameResponse)
def read_game(
    game_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    game = db.query(models.Game).filter(models.Game.id == game_id).first()
    if game is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game not found"
        )
    return game


@router.put("/{game_id}", response_model=schemas.GameResponse)
def update_game(
    game_id: int,
    game_update: schemas.GameUpdate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update game (only owner can update)"""
    game = db.query(models.Game).filter(models.Game.id == game_id).first()
    if game is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game not found"
        )
    
    if game.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this game"
        )
    
    update_data = game_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(game, field, value)
    
    db.commit()
    db.refresh(game)
    return game


@router.delete("/{game_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_game(
    game_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete game (only owner can delete)"""
    game = db.query(models.Game).filter(models.Game.id == game_id).first()
    if game is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game not found"
        )
    
    # Check if current user is the owner
    if game.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this game"
        )
    
    db.delete(game)
    db.commit()
    return None

