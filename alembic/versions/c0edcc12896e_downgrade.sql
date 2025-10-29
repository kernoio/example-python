-- Downgrade migration: revert users and games tables
-- Revision ID: c0edcc12896e
-- Revises to: (base)
-- Create Date: 2025-10-29

BEGIN;

-- Running downgrade c0edcc12896e -> base

DROP TABLE IF EXISTS games;

DROP TABLE IF EXISTS users;

DELETE FROM alembic_version WHERE alembic_version.version_num = 'c0edcc12896e';

DROP TABLE alembic_version;

COMMIT;

