"""empty message

Revision ID: 36944ba86c55
Revises: 206d8c063ef3
Create Date: 2018-12-08 23:06:41.123987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36944ba86c55'
down_revision = '206d8c063ef3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('airport', sa.Column('slug', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('airport', 'slug')
    # ### end Alembic commands ###