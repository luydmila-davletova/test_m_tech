"""fix

Revision ID: 56bf19538812
Revises: 93131623579c
Create Date: 2023-12-14 11:47:34.980655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56bf19538812'
down_revision = '93131623579c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ip_address', sa.String(), nullable=True),
    sa.Column('http_method', sa.String(), nullable=True),
    sa.Column('uri', sa.String(), nullable=True),
    sa.Column('status_code', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_log_ip_address'), 'log', ['ip_address'], unique=False)
    op.drop_index('ix_logs_id', table_name='logs')
    op.drop_index('ix_logs_ip_address', table_name='logs')
    op.drop_table('logs')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('logs',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('ip_address', sa.VARCHAR(), nullable=True),
    sa.Column('http_method', sa.VARCHAR(), nullable=True),
    sa.Column('uri', sa.VARCHAR(), nullable=True),
    sa.Column('status_code', sa.INTEGER(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_logs_ip_address', 'logs', ['ip_address'], unique=False)
    op.create_index('ix_logs_id', 'logs', ['id'], unique=False)
    op.drop_index(op.f('ix_log_ip_address'), table_name='log')
    op.drop_table('log')
    # ### end Alembic commands ###
