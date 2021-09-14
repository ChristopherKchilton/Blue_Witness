"""Added Conversations table, related force_ranks and conversations, changed force_ranks.incident_date from text type to date type

Revision ID: 849e0da20002
Revises: 
Create Date: 2021-08-22 22:32:22.983368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '849e0da20002'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bot_scripts',
    sa.Column('script_id', sa.Integer(), nullable=False),
    sa.Column('script', sa.String(length=255), nullable=True),
    sa.Column('convo_node', sa.Integer(), nullable=True),
    sa.Column('use_count', sa.Integer(), nullable=True),
    sa.Column('positive_count', sa.Integer(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('script_id'),
    sa.UniqueConstraint('script_id')
    )
    op.create_table('script_testing',
    sa.Column('incident_id', sa.Integer(), nullable=False),
    sa.Column('script_path', sa.String(length=100), nullable=True),
    sa.Column('success', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('incident_id'),
    sa.UniqueConstraint('incident_id')
    )
    op.create_table('conversations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('incident_id', sa.Integer(), nullable=True),
    sa.Column('tweet_id', sa.String(length=255), nullable=True),
    sa.Column('form', sa.Integer(), nullable=True),
    sa.Column('root_tweet_city', sa.String(length=255), nullable=True),
    sa.Column('root_tweet_state', sa.String(length=255), nullable=True),
    sa.Column('root_tweet_lat', sa.Float(), nullable=True),
    sa.Column('root_tweet_long', sa.Float(), nullable=True),
    sa.Column('root_tweet_date', sa.Date(), nullable=True),
    sa.Column('root_tweet_force_rank', sa.String(length=255), nullable=True),
    sa.Column('sent_tweet_id', sa.String(), nullable=True),
    sa.Column('received_tweet_id', sa.String(), nullable=True),
    sa.Column('in_reply_to_id', sa.String(), nullable=True),
    sa.Column('tweeter_id', sa.String(), nullable=True),
    sa.Column('conversation_status', sa.Integer(), nullable=True),
    sa.Column('tweet_text', sa.String(), nullable=True),
    sa.Column('checks_made', sa.Integer(), nullable=True),
    sa.Column('reachout_template', sa.String(), nullable=True),
    sa.Column('isChecked', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['incident_id'], ['force_ranks.incident_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sources',
    sa.Column('source_id', sa.Integer(), nullable=False),
    sa.Column('incident_id', sa.Integer(), nullable=True),
    sa.Column('source', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['incident_id'], ['force_ranks.incident_id'], ),
    sa.PrimaryKeyConstraint('source_id'),
    sa.UniqueConstraint('source_id')
    )
    op.create_table('tags',
    sa.Column('tags_id', sa.Integer(), nullable=False),
    sa.Column('incident_id', sa.Integer(), nullable=True),
    sa.Column('tag', sa.String(length=40), nullable=True),
    sa.ForeignKeyConstraint(['incident_id'], ['force_ranks.incident_id'], ),
    sa.PrimaryKeyConstraint('tags_id'),
    sa.UniqueConstraint('tags_id')
    )
    op.alter_column('force_ranks', 'incident_date',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('force_ranks', 'description',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('force_ranks', 'status',
               existing_type=sa.TEXT(),
               nullable=False)
    op.create_unique_constraint(None, 'force_ranks', ['incident_id'])
    op.alter_column('training', 'tweets',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('training', 'labels',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('training', 'labels',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('training', 'tweets',
               existing_type=sa.TEXT(),
               nullable=False)
    op.drop_constraint(None, 'force_ranks', type_='unique')
    op.alter_column('force_ranks', 'status',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('force_ranks', 'description',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('force_ranks', 'incident_date',
               existing_type=sa.DATE(),
               nullable=True)
    op.drop_table('tags')
    op.drop_table('sources')
    op.drop_table('conversations')
    op.drop_table('script_testing')
    op.drop_table('bot_scripts')
    # ### end Alembic commands ###
