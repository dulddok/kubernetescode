"""empty message

Revision ID: 07ca18bf0451
Revises: 
Create Date: 2019-02-27 02:13:01.305589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07ca18bf0451'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('deadline', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todos')
    # ### end Alembic commands ###