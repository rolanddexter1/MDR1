"""empty message

Revision ID: c6e7fc37ad42
Revises: 551c4e6d4a8b
Create Date: 2019-07-22 19:54:23.039909

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6e7fc37ad42'
down_revision = '551c4e6d4a8b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('client_user', sa.Column('default_avatar', sa.Boolean(), server_default='0', nullable=False))
    op.add_column('client_user', sa.Column('name', sa.String(length=128), server_default=sa.text('NULL'), nullable=True))
    op.add_column('gen_email', sa.Column('custom', sa.Boolean(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('gen_email', 'custom')
    op.drop_column('client_user', 'name')
    op.drop_column('client_user', 'default_avatar')
    # ### end Alembic commands ###
