"""empty message

Revision ID: e7253e8d7ee0
Revises: 
Create Date: 2020-04-03 10:18:18.779895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7253e8d7ee0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('class_photos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img_filename', sa.String(), nullable=True),
    sa.Column('week', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student_photos',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('student_name', sa.String(length=80), nullable=False),
    sa.Column('student_photo', sa.String(), nullable=True),
    sa.Column('student_section', sa.String(), nullable=True),
    sa.Column('encodings', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('student_id'),
    sa.UniqueConstraint('student_name')
    )
    op.create_table('student_attendance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('present', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['student_photos.student_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student_attendance')
    op.drop_table('student_photos')
    op.drop_table('class_photos')
    # ### end Alembic commands ###
