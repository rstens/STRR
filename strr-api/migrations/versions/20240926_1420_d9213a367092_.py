"""empty message

Revision ID: d9213a367092
Revises: 144db4d9467d
Create Date: 2024-09-26 14:20:01.253884

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd9213a367092'
down_revision = '144db4d9467d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('application', schema=None) as batch_op:
        batch_op.add_column(sa.Column('application_number', sa.String(length=14), nullable=False))
        batch_op.create_unique_constraint(None, ['application_number'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('application', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('application_number')
    # ### end Alembic commands ###