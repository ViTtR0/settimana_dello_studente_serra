"""empty message

Revision ID: 25cb57daf66b
Revises: 301258c64f5f
Create Date: 2021-12-31 23:55:39.717617

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25cb57daf66b'
down_revision = '301258c64f5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orari_materie_classi')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orari_materie_classi',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('id_orario', sa.INTEGER(), nullable=False),
    sa.Column('id_materia', sa.INTEGER(), nullable=False),
    sa.Column('id_classe', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###