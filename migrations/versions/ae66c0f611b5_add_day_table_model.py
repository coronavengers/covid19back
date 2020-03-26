"""Add day table model

Revision ID: ae66c0f611b5
Revises: 
Create Date: 2020-03-25 22:23:06.137093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae66c0f611b5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('day',
    sa.Column('did', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('did')
    )
    op.create_index(op.f('ix_day_date'), 'day', ['date'], unique=False)
    op.create_index(op.f('ix_day_timestamp'), 'day', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_day_timestamp'), table_name='day')
    op.drop_index(op.f('ix_day_date'), table_name='day')
    op.drop_table('day')
    # ### end Alembic commands ###
