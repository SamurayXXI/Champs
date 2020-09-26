"""Added Champ table 1

Revision ID: 2c4d4895bb89
Revises: ead348fcc18d
Create Date: 2020-09-27 00:46:19.537673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c4d4895bb89'
down_revision = 'ead348fcc18d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('champ',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('national', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_champ_id'), 'champ', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_champ_id'), table_name='champ')
    op.drop_table('champ')
    # ### end Alembic commands ###