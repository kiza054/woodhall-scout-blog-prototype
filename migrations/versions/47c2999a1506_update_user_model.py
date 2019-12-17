"""update user model

Revision ID: 47c2999a1506
Revises: 6a93be8d57c4
Create Date: 2019-11-24 17:48:00.972670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47c2999a1506'
down_revision = '6a93be8d57c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('childs_section', sa.String(length=20), nullable=True))
    op.add_column('user', sa.Column('leader', sa.String(length=6), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'leader')
    op.drop_column('user', 'childs_section')
    # ### end Alembic commands ###