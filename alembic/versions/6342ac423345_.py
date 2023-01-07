"""Forgot to add the revision name. This revision has been created to add missing columns
to my tables in postgres

Revision ID: 6342ac423345
Revises: cb6a96525a92
Create Date: 2023-01-05 15:49:18.701759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6342ac423345'
down_revision = 'cb6a96525a92'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False,
                                     server_default=sa.text("now()")))
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
