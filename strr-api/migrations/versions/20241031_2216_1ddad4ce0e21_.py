"""empty message

Revision ID: 1ddad4ce0e21
Revises: 14f84cc80367
Create Date: 2024-10-31 22:16:54.409155

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1ddad4ce0e21'
down_revision = '14f84cc80367'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    contacttype = postgresql.ENUM('INDIVIDUAL', 'BUSINESS', name='contacttype')
    contacttype.create(op.get_bind(), checkfirst=True)

    with op.batch_alter_table('property_contacts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('contact_type', contacttype, nullable=True))
        batch_op.add_column(sa.Column('business_legal_name', sa.String(length=1000), nullable=True))

    with op.batch_alter_table('property_contacts_history', schema=None) as batch_op:
        batch_op.add_column(sa.Column('contact_type', contacttype, autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('business_legal_name', sa.String(length=1000), autoincrement=False, nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('property_contacts_history', schema=None) as batch_op:
        batch_op.drop_column('business_legal_name')
        batch_op.drop_column('contact_type')

    with op.batch_alter_table('property_contacts', schema=None) as batch_op:
        batch_op.drop_column('business_legal_name')
        batch_op.drop_column('contact_type')

    # ### end Alembic commands ###