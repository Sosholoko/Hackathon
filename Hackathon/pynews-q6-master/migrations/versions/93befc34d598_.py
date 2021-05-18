"""empty message

Revision ID: 93befc34d598
Revises: 
Create Date: 2021-05-09 20:38:44.359974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93befc34d598'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('candidate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=64), nullable=True),
    sa.Column('lastname', sa.String(length=64), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('location', sa.String(length=64), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('nationality', sa.String(length=64), nullable=True),
    sa.Column('origin', sa.String(length=64), nullable=True),
    sa.Column('father_job', sa.String(length=64), nullable=True),
    sa.Column('mother_job', sa.String(length=64), nullable=True),
    sa.Column('father_origin', sa.String(length=64), nullable=True),
    sa.Column('mother_origin', sa.String(length=64), nullable=True),
    sa.Column('school', sa.String(length=64), nullable=True),
    sa.Column('future_job', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mail', sa.String(length=64), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=64), nullable=True),
    sa.Column('boolean', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('candidate')
    # ### end Alembic commands ###