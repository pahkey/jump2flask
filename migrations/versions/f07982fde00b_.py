"""empty message

Revision ID: f07982fde00b
Revises: 6fa514451b58
Create Date: 2022-04-04 22:18:12.857476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f07982fde00b'
down_revision = '6fa514451b58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_user_email'), ['email'])
        batch_op.create_unique_constraint(batch_op.f('uq_user_username'), ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_username'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_user_email'), type_='unique')

    # ### end Alembic commands ###
