"""empty message

Revision ID: 0be766af65ea
Revises: a3c9d7aec165
Create Date: 2024-07-29 04:43:45.762425

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0be766af65ea'
down_revision = 'a3c9d7aec165'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('registrations', schema=None) as batch_op:
        batch_op.add_column(sa.Column('start_date', sa.DateTime(timezone=True), nullable=True))
        batch_op.add_column(sa.Column('end_date', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('registrations', schema=None) as batch_op:
        # Remove the new columns
        batch_op.drop_column('end_date')
        batch_op.drop_column('start_date')
    # ### end Alembic commands ###