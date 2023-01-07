"""add content column to post table

Revision ID: e9c1bec97033
Revises: 0e9717782d99
Create Date: 2023-01-05 15:24:01.397244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9c1bec97033'
down_revision = '0e9717782d99'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
