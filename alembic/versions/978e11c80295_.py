"""empty message

Revision ID: 978e11c80295
Revises: ee8e3d83e280
Create Date: 2020-07-14 01:37:59.773490

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '978e11c80295'
down_revision = 'ee8e3d83e280'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('guild')
    op.add_column('guild_members', sa.Column('present', sa.Boolean(), nullable=True))
    op.create_foreign_key(None, 'guild_members', 'guilds', ['guild_id'], ['id'])
    op.create_foreign_key(None, 'guild_members', 'users', ['user_id'], ['id'])
    op.drop_column('guild_members', 'join_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('guild_members', sa.Column('join_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'guild_members', type_='foreignkey')
    op.drop_constraint(None, 'guild_members', type_='foreignkey')
    op.drop_column('guild_members', 'present')
    op.create_table('guild',
    sa.Column('uuid', postgresql.UUID(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('guild_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='guild_pkey'),
    sa.UniqueConstraint('guild_id', name='guild_guild_id_key'),
    sa.UniqueConstraint('uuid', name='guild_uuid_key')
    )
    # ### end Alembic commands ###
