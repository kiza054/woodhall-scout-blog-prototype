"""tasks

Revision ID: b66bd87e2b49
Revises: 47c2999a1506
Create Date: 2019-12-04 12:49:34.102796

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b66bd87e2b49'
down_revision = '47c2999a1506'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('complete', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_task_name'), ['name'], unique=False)

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('attachments_file_path')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('attachments_file_path', sa.VARCHAR(length=300), nullable=True))

    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_task_name'))

    op.drop_table('task')
    # ### end Alembic commands ###
