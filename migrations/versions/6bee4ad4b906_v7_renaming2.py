"""v7 renaming2

Revision ID: 6bee4ad4b906
Revises: d108b7b700da
Create Date: 2019-08-06 14:25:27.049990

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6bee4ad4b906'
down_revision = 'd108b7b700da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Daily', sa.Column('arest_time', sa.Time(), nullable=True))
    op.add_column('Daily', sa.Column('awork_pay', sa.Integer(), nullable=True))
    op.add_column('Daily', sa.Column('awork_time', sa.Time(), nullable=True))
    op.add_column('Daily', sa.Column('crest_time', sa.Time(), nullable=True))
    op.add_column('Daily', sa.Column('cwork_pay', sa.Integer(), nullable=True))
    op.add_column('Daily', sa.Column('cwork_time', sa.Time(), nullable=True))
    op.add_column('Daily', sa.Column('holy_pay', sa.Integer(), nullable=True))
    op.add_column('Daily', sa.Column('holy_time', sa.Time(), nullable=True))
    op.drop_column('Daily', 'holiday_time')
    op.drop_column('Daily', 'actual_pay')
    op.drop_column('Daily', 'contract_pay')
    op.drop_column('Daily', 'holiday_pay')
    op.drop_column('Daily', 'contract_work_time')
    op.drop_column('Daily', 'actual_work_time')
    op.drop_column('Daily', 'contract_rest_time')
    op.drop_column('Daily', 'actual_rest_time')
    op.add_column('Monthly', sa.Column('arest_mtime', sa.Time(), nullable=True))
    op.add_column('Monthly', sa.Column('awork_mpay', sa.Integer(), nullable=True))
    op.add_column('Monthly', sa.Column('awork_mtime', sa.Time(), nullable=True))
    op.add_column('Monthly', sa.Column('crest_mtime', sa.Time(), nullable=True))
    op.add_column('Monthly', sa.Column('cwork_mpay', sa.Integer(), nullable=True))
    op.add_column('Monthly', sa.Column('cwork_mtime', sa.Time(), nullable=True))
    op.add_column('Monthly', sa.Column('holy_mpay', sa.Integer(), nullable=True))
    op.add_column('Monthly', sa.Column('holy_mtime', sa.Time(), nullable=True))
    op.drop_constraint('monthly_ibfk_1', 'Monthly', type_='foreignkey')
    op.create_foreign_key(None, 'Monthly', 'WorkContract', ['cont_id'], ['cont_id'])
    op.drop_column('Monthly', 'holiday_mtime')
    op.drop_column('Monthly', 'actual_mpay')
    op.drop_column('Monthly', 'holiday_mpay')
    op.drop_column('Monthly', 'contract_work_mtime')
    op.drop_column('Monthly', 'contract_rest_mtime')
    op.drop_column('Monthly', 'contract_mpay')
    op.drop_column('Monthly', 'actual_rest_mtime')
    op.drop_column('Monthly', 'actual_work_mtime')
    op.drop_constraint('weekly_ibfk_1', 'Weekly', type_='foreignkey')
    op.create_foreign_key(None, 'Weekly', 'WorkContract', ['cont_id'], ['cont_id'])
    op.add_column('WorkCondition', sa.Column('arest_time', sa.Time(), nullable=True))
    op.add_column('WorkCondition', sa.Column('awork_time', sa.Time(), nullable=True))
    op.drop_constraint('workcondition_ibfk_1', 'WorkCondition', type_='foreignkey')
    op.create_foreign_key(None, 'WorkCondition', 'WorkContract', ['cont_id'], ['cont_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.drop_column('WorkCondition', 'work_aot')
    op.drop_column('WorkCondition', 'rest_aot')
    op.drop_constraint('workcontract_ibfk_1', 'WorkContract', type_='foreignkey')
    op.drop_constraint('workcontract_ibfk_2', 'WorkContract', type_='foreignkey')
    op.create_foreign_key(None, 'WorkContract', 'WorkPlace', ['wp_id'], ['wp_id'])
    op.create_foreign_key(None, 'WorkContract', 'User', ['user_id'], ['user_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'WorkContract', type_='foreignkey')
    op.drop_constraint(None, 'WorkContract', type_='foreignkey')
    op.create_foreign_key('workcontract_ibfk_2', 'WorkContract', 'workplace', ['wp_id'], ['wp_id'])
    op.create_foreign_key('workcontract_ibfk_1', 'WorkContract', 'user', ['user_id'], ['user_id'])
    op.add_column('WorkCondition', sa.Column('rest_aot', mysql.TIME(), nullable=True))
    op.add_column('WorkCondition', sa.Column('work_aot', mysql.TIME(), nullable=True))
    op.drop_constraint(None, 'WorkCondition', type_='foreignkey')
    op.create_foreign_key('workcondition_ibfk_1', 'WorkCondition', 'workcontract', ['cont_id'], ['cont_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.drop_column('WorkCondition', 'awork_time')
    op.drop_column('WorkCondition', 'arest_time')
    op.drop_constraint(None, 'Weekly', type_='foreignkey')
    op.create_foreign_key('weekly_ibfk_1', 'Weekly', 'workcontract', ['cont_id'], ['cont_id'])
    op.add_column('Monthly', sa.Column('actual_work_mtime', mysql.TIME(), nullable=True))
    op.add_column('Monthly', sa.Column('actual_rest_mtime', mysql.TIME(), nullable=True))
    op.add_column('Monthly', sa.Column('contract_mpay', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('Monthly', sa.Column('contract_rest_mtime', mysql.TIME(), nullable=True))
    op.add_column('Monthly', sa.Column('contract_work_mtime', mysql.TIME(), nullable=True))
    op.add_column('Monthly', sa.Column('holiday_mpay', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('Monthly', sa.Column('actual_mpay', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('Monthly', sa.Column('holiday_mtime', mysql.TIME(), nullable=True))
    op.drop_constraint(None, 'Monthly', type_='foreignkey')
    op.create_foreign_key('monthly_ibfk_1', 'Monthly', 'workcontract', ['cont_id'], ['cont_id'])
    op.drop_column('Monthly', 'holy_mtime')
    op.drop_column('Monthly', 'holy_mpay')
    op.drop_column('Monthly', 'cwork_mtime')
    op.drop_column('Monthly', 'cwork_mpay')
    op.drop_column('Monthly', 'crest_mtime')
    op.drop_column('Monthly', 'awork_mtime')
    op.drop_column('Monthly', 'awork_mpay')
    op.drop_column('Monthly', 'arest_mtime')
    op.add_column('Daily', sa.Column('actual_rest_time', mysql.TIME(), nullable=True))
    op.add_column('Daily', sa.Column('contract_rest_time', mysql.TIME(), nullable=True))
    op.add_column('Daily', sa.Column('actual_work_time', mysql.TIME(), nullable=True))
    op.add_column('Daily', sa.Column('contract_work_time', mysql.TIME(), nullable=True))
    op.add_column('Daily', sa.Column('holiday_pay', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('Daily', sa.Column('contract_pay', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('Daily', sa.Column('actual_pay', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('Daily', sa.Column('holiday_time', mysql.TIME(), nullable=True))
    op.drop_column('Daily', 'holy_time')
    op.drop_column('Daily', 'holy_pay')
    op.drop_column('Daily', 'cwork_time')
    op.drop_column('Daily', 'cwork_pay')
    op.drop_column('Daily', 'crest_time')
    op.drop_column('Daily', 'awork_time')
    op.drop_column('Daily', 'awork_pay')
    op.drop_column('Daily', 'arest_time')
    # ### end Alembic commands ###