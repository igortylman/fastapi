"""add votes table

Revision ID: 1cede92cafc3
Revises: 6342ac423345
Create Date: 2023-01-05 16:22:36.732538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cede92cafc3'
down_revision = '6342ac423345'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.drop_constraint('posts_users_fk', 'posts', type_='foreignkey')
    op.create_foreign_key(None, 'posts', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_column('posts', 'owner_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.create_foreign_key('posts_users_fk', 'posts', 'users', ['owner_id'], ['id'], ondelete='CASCADE')
    op.drop_column('posts', 'user_id')
    op.drop_table('votes')
    # ### end Alembic commands ###