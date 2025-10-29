-- Initial migration with users and games tables
-- Revision ID: c0edcc12896e
-- Revises: 
-- Create Date: 2025-10-29

BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> c0edcc12896e

CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username VARCHAR NOT NULL UNIQUE,
            email VARCHAR NOT NULL UNIQUE,
            hashed_password VARCHAR NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

CREATE INDEX ix_users_username ON users(username);

CREATE INDEX ix_users_email ON users(email);

CREATE INDEX ix_users_id ON users(id);

CREATE TABLE games (
            id SERIAL PRIMARY KEY,
            title VARCHAR NOT NULL,
            description VARCHAR,
            genre VARCHAR,
            owner_id INTEGER NOT NULL REFERENCES users(id),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

CREATE INDEX ix_games_title ON games(title);

CREATE INDEX ix_games_id ON games(id);

INSERT INTO alembic_version (version_num) VALUES ('c0edcc12896e') RETURNING alembic_version.version_num;

COMMIT;

