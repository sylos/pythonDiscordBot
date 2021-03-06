"""Added Command Records table

Revision ID: 53bee924b609
Revises: 5f1503cb4245
Create Date: 2020-06-29 01:06:16.706305

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '53bee924b609'
down_revision = '5f1503cb4245'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('message')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('message',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('uuid', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('author', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('content', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('guild', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('messages_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('channel', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='message_pkey'),
    sa.UniqueConstraint('uuid', name='message_uuid_key')
    )
    # ### end Alembic commands ###
