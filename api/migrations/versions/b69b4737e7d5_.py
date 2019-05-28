"""empty message

Revision ID: b69b4737e7d5
Revises: e3462d62f361
Create Date: 2018-12-09 00:20:44.685031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b69b4737e7d5'
down_revision = 'e3462d62f361'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('airline', sa.Column('icao', sa.String(length=4), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('airline', 'icao')
    # ### end Alembic commands ###