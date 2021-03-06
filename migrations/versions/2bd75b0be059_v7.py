"""v7

Revision ID: 2bd75b0be059
Revises: 
Create Date: 2019-08-06 13:22:27.473599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bd75b0be059'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('BlacklistTokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('CategoryLaw',
    sa.Column('law_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('applied_date', sa.DateTime(), nullable=True),
    sa.Column('minimum_wage', sa.Integer(), nullable=True),
    sa.Column('law_02', sa.Integer(), nullable=True),
    sa.Column('law_03', sa.Integer(), nullable=True),
    sa.Column('created_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('law_id')
    )
    op.create_table('Daily',
    sa.Column('daliy_id', sa.String(length=50), nullable=False),
    sa.Column('wcond_id', sa.Integer(), nullable=False),
    sa.Column('cont_id', sa.String(length=45), nullable=False),
    sa.Column('target_ym', sa.String(length=6), nullable=False),
    sa.Column('target_date', sa.String(length=2), nullable=False),
    sa.Column('week_num', sa.Integer(), nullable=True),
    sa.Column('day_num', sa.Integer(), nullable=True),
    sa.Column('work_start', sa.DateTime(), nullable=True),
    sa.Column('work_end', sa.DateTime(), nullable=True),
    sa.Column('actual_work_time', sa.Time(), nullable=True),
    sa.Column('contract_work_time', sa.Time(), nullable=True),
    sa.Column('actual_rest_time', sa.Time(), nullable=True),
    sa.Column('contract_rest_time', sa.Time(), nullable=True),
    sa.Column('over_work_time', sa.Time(), nullable=True),
    sa.Column('night_work_time', sa.Time(), nullable=True),
    sa.Column('holiday_work_time', sa.Time(), nullable=True),
    sa.Column('actual_work_pay', sa.Integer(), nullable=True),
    sa.Column('contract_work_pay', sa.Integer(), nullable=True),
    sa.Column('over_work_pay', sa.Integer(), nullable=True),
    sa.Column('night_work_pay', sa.Integer(), nullable=True),
    sa.Column('holiday_work_pay', sa.Integer(), nullable=True),
    sa.Column('total_work_pay', sa.Integer(), nullable=True),
    sa.Column('created_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('daliy_id', 'target_ym', 'target_date')
    )
    op.create_table('FAQ',
    sa.Column('faq_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('group', sa.Integer(), nullable=True),
    sa.Column('sequence', sa.Integer(), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=45), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('active', sa.Integer(), nullable=True),
    sa.Column('created_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('faq_id')
    )
    op.create_table('IncomeTax',
    sa.Column('more', sa.Integer(), nullable=False),
    sa.Column('under', sa.Integer(), nullable=False),
    sa.Column('p_1', sa.Integer(), nullable=True),
    sa.Column('p_2', sa.Integer(), nullable=True),
    sa.Column('p_3', sa.Integer(), nullable=True),
    sa.Column('p_4', sa.Integer(), nullable=True),
    sa.Column('p_5', sa.Integer(), nullable=True),
    sa.Column('p_6', sa.Integer(), nullable=True),
    sa.Column('p_7', sa.Integer(), nullable=True),
    sa.Column('p_8', sa.Integer(), nullable=True),
    sa.Column('p_9', sa.Integer(), nullable=True),
    sa.Column('p_10', sa.Integer(), nullable=True),
    sa.Column('p_11', sa.Integer(), nullable=True),
    sa.Column('apply_date', sa.String(length=6, collation='utf8mb4_unicode_ci'), nullable=True),
    sa.PrimaryKeyConstraint('more', 'under')
    )
    op.create_table('TermsAgreement',
    sa.Column('terms_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('terms_01', sa.Integer(), nullable=True),
    sa.Column('terms_02', sa.Integer(), nullable=True),
    sa.Column('terms_03', sa.Integer(), nullable=True),
    sa.Column('created_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('terms_id')
    )
    op.create_table('TimeCard',
    sa.Column('tc_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cont_id', sa.Integer(), nullable=False),
    sa.Column('wcond_id', sa.Integer(), nullable=False),
    sa.Column('target_ym', sa.String(length=6), nullable=False),
    sa.Column('target_date', sa.String(length=2), nullable=False),
    sa.Column('type_code', sa.Integer(), nullable=False),
    sa.Column('in_time', sa.DateTime(), nullable=True),
    sa.Column('created_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('tc_id', 'cont_id', 'wcond_id', 'target_ym', 'target_date')
    )
    op.create_table('TimeCardMemo',
    sa.Column('tcmemo_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tc_id', sa.Integer(), nullable=False),
    sa.Column('target_ym', sa.String(length=6), nullable=False),
    sa.Column('target_date', sa.String(length=2), nullable=False),
    sa.Column('article', sa.Text(), nullable=True),
    sa.Column('having_photo', sa.String(length=255), nullable=True),
    sa.Column('created_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('tcmemo_id')
    )
    op.create_table('User',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.String(length=16), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('birth', sa.Integer(), nullable=True),
    sa.Column('sex', sa.Integer(), nullable=True),
    sa.Column('password_hash', sa.String(length=100), nullable=True),
    sa.Column('user_status', sa.Integer(), server_default='1', nullable=False),
    sa.Column('admin', sa.Boolean(), server_default='0', nullable=False),
    sa.Column('created_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('WorkPlace',
    sa.Column('wp_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('wp_name', sa.String(length=45), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('kakao_place_id', sa.String(length=45), nullable=True),
    sa.Column('road_address', sa.String(length=255), nullable=True),
    sa.Column('category_name', sa.String(length=255), nullable=True),
    sa.Column('phone', sa.String(length=255), nullable=True),
    sa.Column('bjd_code', sa.String(length=10), nullable=True),
    sa.Column('building_name', sa.String(length=255), nullable=True),
    sa.Column('business_code', sa.String(length=45), nullable=True),
    sa.Column('owner', sa.String(length=45), nullable=True),
    sa.Column('over_5employee', sa.Integer(), server_default='1', nullable=True),
    sa.Column('x', sa.Text(), nullable=True),
    sa.Column('y', sa.Text(), nullable=True),
    sa.Column('created_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('wp_id')
    )
    op.create_table('Yearly',
    sa.Column('yearly_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cont_id', sa.Integer(), nullable=False),
    sa.Column('created_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('yearly_id')
    )
    op.create_table('WorkContract',
    sa.Column('cont_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('wp_id', sa.Integer(), nullable=False),
    sa.Column('cont_date', sa.String(length=8), nullable=False),
    sa.Column('first_start_date', sa.String(length=8), nullable=True),
    sa.Column('1_start_pot', sa.Time(), nullable=True),
    sa.Column('1_end_pot', sa.Time(), nullable=True),
    sa.Column('1_rest_aot', sa.Time(), nullable=True),
    sa.Column('2_start_pot', sa.Time(), nullable=True),
    sa.Column('2_end_pot', sa.Time(), nullable=True),
    sa.Column('2_rest_aot', sa.Time(), nullable=True),
    sa.Column('3_start_pot', sa.Time(), nullable=True),
    sa.Column('3_end_pot', sa.Time(), nullable=True),
    sa.Column('3_rest_aot', sa.Time(), nullable=True),
    sa.Column('4_start_pot', sa.Time(), nullable=True),
    sa.Column('4_end_pot', sa.Time(), nullable=True),
    sa.Column('4_rest_aot', sa.Time(), nullable=True),
    sa.Column('5_start_pot', sa.Time(), nullable=True),
    sa.Column('5_end_pot', sa.Time(), nullable=True),
    sa.Column('5_rest_aot', sa.Time(), nullable=True),
    sa.Column('6_start_pot', sa.Time(), nullable=True),
    sa.Column('6_end_pot', sa.Time(), nullable=True),
    sa.Column('6_rest_aot', sa.Time(), nullable=True),
    sa.Column('7_start_pot', sa.Time(), nullable=True),
    sa.Column('7_end_pot', sa.Time(), nullable=True),
    sa.Column('7_rest_aot', sa.Time(), nullable=True),
    sa.Column('week_holiday', sa.Integer(), nullable=True),
    sa.Column('work_day_cnt', sa.Integer(), nullable=True),
    sa.Column('hourly_pay', sa.Integer(), nullable=True),
    sa.Column('monthly_pay', sa.Integer(), nullable=True),
    sa.Column('pay_init_day', sa.Integer(), server_default='1', nullable=True),
    sa.Column('pay_day', sa.Integer(), server_default='10', nullable=True),
    sa.Column('work_time_offset', sa.Time(), server_default='00:05:00', nullable=True),
    sa.Column('having_photo', sa.String(length=255), nullable=True),
    sa.Column('cont_status', sa.Integer(), server_default='1', nullable=False),
    sa.Column('created_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['User.user_id'], ),
    sa.ForeignKeyConstraint(['wp_id'], ['WorkPlace.wp_id'], ),
    sa.PrimaryKeyConstraint('cont_id', 'cont_date')
    )
    op.create_index(op.f('ix_WorkContract_user_id'), 'WorkContract', ['user_id'], unique=False)
    op.create_index(op.f('ix_WorkContract_wp_id'), 'WorkContract', ['wp_id'], unique=False)
    op.create_table('Monthly',
    sa.Column('monthly_id', sa.String(length=50), nullable=False),
    sa.Column('cont_id', sa.Integer(), nullable=False),
    sa.Column('target_ym', sa.String(length=6), nullable=True),
    sa.Column('start_mdate', sa.String(length=8), nullable=True),
    sa.Column('end_mdate', sa.String(length=8), nullable=True),
    sa.Column('actual_work_mtime', sa.Time(), nullable=True),
    sa.Column('contract_work_mtime', sa.Time(), nullable=True),
    sa.Column('actual_rest_time', sa.Time(), nullable=True),
    sa.Column('contract_rest_mtime', sa.Time(), nullable=True),
    sa.Column('over_work_mtime', sa.Time(), nullable=True),
    sa.Column('night_work_mtime', sa.Time(), nullable=True),
    sa.Column('holiday_work_mtime', sa.Time(), nullable=True),
    sa.Column('actual_work_mpay', sa.Integer(), nullable=True),
    sa.Column('contract_work_mpay', sa.Integer(), nullable=True),
    sa.Column('over_work_mpay', sa.Integer(), nullable=True),
    sa.Column('night_work_mpay', sa.Integer(), nullable=True),
    sa.Column('holiday_work_mpay', sa.Integer(), nullable=True),
    sa.Column('total_work_mpay', sa.Integer(), nullable=True),
    sa.Column('weekly_mpay', sa.Integer(), nullable=True),
    sa.Column('total_days', sa.Integer(), nullable=True),
    sa.Column('national_pension', sa.Integer(), nullable=True),
    sa.Column('health_insurance', sa.Integer(), nullable=True),
    sa.Column('employment_insurance', sa.Integer(), nullable=True),
    sa.Column('income_tax', sa.Integer(), nullable=True),
    sa.Column('tax_exemption', sa.Integer(), nullable=True),
    sa.Column('after_deduction', sa.Integer(), nullable=True),
    sa.Column('created_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['cont_id'], ['WorkContract.cont_id'], ),
    sa.PrimaryKeyConstraint('monthly_id')
    )
    op.create_index(op.f('ix_Monthly_cont_id'), 'Monthly', ['cont_id'], unique=False)
    op.create_table('Weekly',
    sa.Column('weekly_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cont_id', sa.Integer(), nullable=False),
    sa.Column('target_ym', sa.String(length=8), nullable=False),
    sa.Column('week_num', sa.Integer(), nullable=True),
    sa.Column('total_work_time', sa.Time(), nullable=True),
    sa.Column('total_work_pay', sa.Integer(), nullable=True),
    sa.Column('week_holy_dnum', sa.Integer(), nullable=True),
    sa.Column('week_holy_pay', sa.Integer(), nullable=True),
    sa.Column('created_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['cont_id'], ['WorkContract.cont_id'], ),
    sa.PrimaryKeyConstraint('weekly_id', 'target_ym')
    )
    op.create_index(op.f('ix_Weekly_cont_id'), 'Weekly', ['cont_id'], unique=False)
    op.create_table('WorkCondition',
    sa.Column('wcond_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cont_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('wp_id', sa.Integer(), nullable=False),
    sa.Column('target_ym', sa.String(length=6), nullable=True),
    sa.Column('target_date', sa.String(length=2), nullable=True),
    sa.Column('week_num', sa.Integer(), nullable=True),
    sa.Column('day_num', sa.Integer(), nullable=True),
    sa.Column('start_work_time', sa.Time(), nullable=True),
    sa.Column('end_work_time', sa.Time(), nullable=True),
    sa.Column('amount_work_time', sa.Time(), nullable=True),
    sa.Column('amount_rest_time', sa.Time(), nullable=True),
    sa.Column('hourly_pay', sa.Integer(), nullable=True),
    sa.Column('daily_pay', sa.Integer(), nullable=True),
    sa.Column('tardiness_code', sa.Integer(), server_default='1', nullable=False),
    sa.Column('wcond_status', sa.Integer(), server_default='1', nullable=False),
    sa.Column('created_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['cont_id'], ['WorkContract.cont_id'], onupdate='RESTRICT', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('wcond_id', 'cont_id')
    )
    op.create_index(op.f('ix_WorkCondition_cont_id'), 'WorkCondition', ['cont_id'], unique=False)
    op.create_index(op.f('ix_WorkCondition_user_id'), 'WorkCondition', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_WorkCondition_user_id'), table_name='WorkCondition')
    op.drop_index(op.f('ix_WorkCondition_cont_id'), table_name='WorkCondition')
    op.drop_table('WorkCondition')
    op.drop_index(op.f('ix_Weekly_cont_id'), table_name='Weekly')
    op.drop_table('Weekly')
    op.drop_index(op.f('ix_Monthly_cont_id'), table_name='Monthly')
    op.drop_table('Monthly')
    op.drop_index(op.f('ix_WorkContract_wp_id'), table_name='WorkContract')
    op.drop_index(op.f('ix_WorkContract_user_id'), table_name='WorkContract')
    op.drop_table('WorkContract')
    op.drop_table('Yearly')
    op.drop_table('WorkPlace')
    op.drop_table('User')
    op.drop_table('TimeCardMemo')
    op.drop_table('TimeCard')
    op.drop_table('TermsAgreement')
    op.drop_table('IncomeTax')
    op.drop_table('FAQ')
    op.drop_table('Daily')
    op.drop_table('CategoryLaw')
    op.drop_table('BlacklistTokens')
    # ### end Alembic commands ###
