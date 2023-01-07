"""add users table

Revision ID: 493d044a223f
Revises: e9c1bec97033
Create Date: 2023-01-05 15:28:41.747705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '493d044a223f'
down_revision = 'e9c1bec97033'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
