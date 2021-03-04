"""empty message

Revision ID: 63ab91c6882e
Revises: cf902fc057fb
Create Date: 2021-03-03 19:33:08.091109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63ab91c6882e'
down_revision = 'cf902fc057fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.String(length=256), nullable=False))
    op.add_column('user', sa.Column('username', sa.String(length=150), nullable=False))
    op.drop_constraint('user_address_key', 'user', type_='unique')
    op.drop_constraint('user_city_key', 'user', type_='unique')
    op.drop_constraint('user_firstName_key', 'user', type_='unique')
    op.drop_constraint('user_lastName_key', 'user', type_='unique')
    op.drop_constraint('user_phoneNum_key', 'user', type_='unique')
    op.drop_constraint('user_state_key', 'user', type_='unique')
    op.create_unique_constraint(None, 'user', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.create_unique_constraint('user_state_key', 'user', ['state'])
    op.create_unique_constraint('user_phoneNum_key', 'user', ['phoneNum'])
    op.create_unique_constraint('user_lastName_key', 'user', ['lastName'])
    op.create_unique_constraint('user_firstName_key', 'user', ['firstName'])
    op.create_unique_constraint('user_city_key', 'user', ['city'])
    op.create_unique_constraint('user_address_key', 'user', ['address'])
    op.drop_column('user', 'username')
    op.drop_column('user', 'password')
    # ### end Alembic commands ###
