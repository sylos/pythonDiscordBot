"""Added created at column to record

Revision ID: 39356c1e6711
Revises: 53bee924b609
Create Date: 2020-06-29 03:53:30.633475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39356c1e6711'
down_revision = '53bee924b609'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('command_record', sa.Column('messaged_created_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('command_record', 'messaged_created_at')
    # ### end Alembic commands ###
