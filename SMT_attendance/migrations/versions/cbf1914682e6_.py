"""empty message

Revision ID: cbf1914682e6
Revises: 6458b5c983c7
Create Date: 2020-03-12 16:43:24.344622

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbf1914682e6'
down_revision = '6458b5c983c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('class_photos_name_key', 'class_photos', type_='unique')
    op.drop_column('class_photos', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('class_photos', sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
    op.create_unique_constraint('class_photos_name_key', 'class_photos', ['name'])
    # ### end Alembic commands ###
