"""empty message

Revision ID: e3ac518de6c6
Revises: adba61262b9b
Create Date: 2021-10-28 18:31:00.895174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3ac518de6c6'
down_revision = 'adba61262b9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vachist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('biznum', sa.String(length=100), nullable=True),
    sa.Column('vacdt', sa.String(length=20), nullable=True),
    sa.Column('req_dt', sa.String(length=20), nullable=True),
    sa.Column('vac_ty', sa.String(length=10), nullable=True),
    sa.Column('vac_ap_ty', sa.String(length=10), nullable=True),
    sa.Column('pro_sts', sa.String(length=10), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('modify_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_vachist_user_id_user'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_vachist'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vachist')
    # ### end Alembic commands ###
