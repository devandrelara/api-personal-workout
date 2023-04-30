"""added workout table and join table

Revision ID: f6e51d9f208c
Revises: 77c294385f1d
Create Date: 2023-04-29 23:33:35.512677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6e51d9f208c'
down_revision = '77c294385f1d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('workouts',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('rest_interval', sa.Integer(), nullable=False),
    sa.Column('recurrence_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['recurrence_id'], ['recurrences.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('workouts_set_blocks',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('set_block_id', sa.UUID(), nullable=True),
    sa.Column('workout_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['set_block_id'], ['set_blocks.id'], ),
    sa.ForeignKeyConstraint(['workout_id'], ['sets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('workouts_set_blocks')
    op.drop_table('workouts')
    # ### end Alembic commands ###
