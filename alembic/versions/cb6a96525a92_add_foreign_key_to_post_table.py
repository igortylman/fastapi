"""add foreign key to post table

Revision ID: cb6a96525a92
Revises: 493d044a223f
Create Date: 2023-01-05 15:42:21.191429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb6a96525a92'
down_revision = '493d044a223f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("posts_users_fk", source_table="posts", referent_table="users",
                          local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
