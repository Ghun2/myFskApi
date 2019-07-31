# coding: utf-8
from app.main import db
from sqlalchemy.sql import func


class CategoryLaw(db.Model):
    __tablename__ = 'CategoryLaw'

    law_id = db.Column(db.Integer, primary_key=True)
    applied_date = db.Column(db.DateTime)
    minimum_wage = db.Column(db.Integer)
    law_02 = db.Column(db.Integer)
    law_03 = db.Column(db.Integer)
    created_time = db.Column(db.DateTime, server_default=func.now())
    updated_time = db.Column(db.DateTime)


class Daily(db.Model):
    __tablename__ = 'Daily'

    daliy_id = db.Column(db.String(50), primary_key=True, nullable=False)
    wcond_id = db.Column(db.ForeignKey('WorkCondition.wcond_id'), nullable=False, index=True)
    cont_id = db.Column(db.String(45), nullable=False)
    target_ym = db.Column(db.String(6), primary_key=True, nullable=False)
    target_date = db.Column(db.String(2), primary_key=True, nullable=False)
    week_num = db.Column(db.Integer)
    day_num = db.Column(db.Integer)
    work_start = db.Column(db.DateTime)
    work_end = db.Column(db.DateTime)
    actual_work_time = db.Column(db.Time)
    contract_work_time = db.Column(db.Time)
    actual_rest_time = db.Column(db.Time)
    contract_rest_time = db.Column(db.Time)
    over_work_time = db.Column(db.Time)
    night_work_time = db.Column(db.Time)
    holiday_work_time = db.Column(db.Time)
    actual_work_pay = db.Column(db.Numeric(12, 2))
    contract_work_pay = db.Column(db.Numeric(12, 2))
    over_work_pay = db.Column(db.Numeric(12, 2))
    night_work_pay = db.Column(db.Numeric(12, 2))
    holiday_work_pay = db.Column(db.Numeric(12, 2))
    total_work_pay = db.Column(db.Numeric(12, 2))
    created_time = db.Column(db.DateTime, server_default=func.now())
    updated_time = db.Column(db.DateTime)

    wcond = db.relationship('WorkCondition', primaryjoin='Daily.wcond_id == WorkCondition.wcond_id', backref='dailies')


class FAQ(db.Model):
    __tablename__ = 'FAQ'

    id = db.Column(db.Integer, primary_key=True)
    group = db.Column(db.Integer)
    sequence = db.Column(db.Integer)
    level = db.Column(db.Integer)
    title = db.Column(db.String(45))
    content = db.Column(db.Text)
    active = db.Column(db.Integer)
    created_time = db.Column(db.DateTime, server_default=func.now())
    updated_time = db.Column(db.DateTime)


class IncomeTax(db.Model):
    __tablename__ = 'IncomeTax'

    more = db.Column(db.Integer, primary_key=True, nullable=False)
    under = db.Column(db.Integer, primary_key=True, nullable=False)
    p_1 = db.Column(db.Integer)
    p_2 = db.Column(db.Integer)
    p_3 = db.Column(db.Integer)
    p_4 = db.Column(db.Integer)
    p_5 = db.Column(db.Integer)
    p_6 = db.Column(db.Integer)
    p_7 = db.Column(db.Integer)
    p_8 = db.Column(db.Integer)
    p_9 = db.Column(db.Integer)
    p_10 = db.Column(db.Integer)
    p_11 = db.Column(db.Integer)
    apply_date = db.Column(db.String(6, 'utf8mb4_unicode_ci'))


class Monthly(db.Model):
    __tablename__ = 'Monthly'

    monthly_id = db.Column(db.String(50, 'utf8mb4_general_ci'), primary_key=True)
    cont_id = db.Column(db.ForeignKey('WorkContract.cont_id'), nullable=False, index=True)
    target_ym = db.Column(db.String(6, 'utf8mb4_0900_ai_ci'))
    start_mdate = db.Column(db.String(8, 'utf8mb4_0900_ai_ci'))
    end_mdate = db.Column(db.String(8, 'utf8mb4_0900_ai_ci'))
    actual_work_mtime = db.Column(db.Time)
    contract_work_mtime = db.Column(db.Time)
    actual_rest_time = db.Column(db.Time)
    contract_rest_mtime = db.Column(db.Time)
    over_work_mtime = db.Column(db.Time)
    night_work_mtime = db.Column(db.Time)
    holiday_work_mtime = db.Column(db.Time)
    actual_work_mpay = db.Column(db.Numeric(12, 2))
    contract_work_mpay = db.Column(db.Numeric(12, 2))
    over_work_mpay = db.Column(db.Numeric(12, 2))
    night_work_mpay = db.Column(db.Numeric(12, 2))
    holiday_work_mpay = db.Column(db.Numeric(12, 2))
    total_work_mpay = db.Column(db.Numeric(12, 2))
    total_days = db.Column(db.Integer)
    national_pension = db.Column(db.Numeric(12, 2))
    health_insurance = db.Column(db.Numeric(12, 2))
    employment_insurance = db.Column(db.Numeric(12, 2))
    income_tax = db.Column(db.Numeric(12, 2))
    tax_exemption = db.Column(db.Numeric(12, 2))
    after_deduction = db.Column(db.Numeric(12, 2))
    created_time = db.Column(db.DateTime, server_default=func.now())
    updated_time = db.Column(db.DateTime)

    cont = db.relationship('WorkContract', primaryjoin='Monthly.cont_id == WorkContract.cont_id', backref='monthlies')


class TermsAgreement(db.Model):
    __tablename__ = 'TermsAgreement'

    terms_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    terms_01 = db.Column(db.Integer)
    terms_02 = db.Column(db.Integer)
    terms_03 = db.Column(db.Integer)
    created_time = db.Column(db.DateTime, server_default=func.now())
    updated_time = db.Column(db.DateTime)


class TimeCard(db.Model):
    __tablename__ = 'TimeCard'

    tc_id = db.Column(db.Integer, primary_key=True, nullable=False)
    wcond_id = db.Column(db.ForeignKey('WorkCondition.wcond_id'), primary_key=True, nullable=False, index=True)
    target_ym = db.Column(db.String(6), primary_key=True, nullable=False)
    target_date = db.Column(db.String(2), primary_key=True, nullable=False)
    type_code = db.Column(db.Integer, nullable=False)
    in_time = db.Column(db.DateTime)
    created_time = db.Column(db.DateTime, server_default=func.now())
    updated_time = db.Column(db.DateTime)

    wcond = db.relationship('WorkCondition', primaryjoin='TimeCard.wcond_id == WorkCondition.wcond_id', backref='time_cards')


class TimeCardMemo(db.Model):
    __tablename__ = 'TimeCardMemo'

    tcmemo_id = db.Column(db.Integer, primary_key=True)
    tc_id = db.Column(db.Integer, nullable=False)
    target_ym = db.Column(db.String(6), nullable=False)
    target_date = db.Column(db.String(2), nullable=False)
    article = db.Column(db.Text)
    having_photo = db.Column(db.String(255))
    created_time = db.Column(db.DateTime, server_default=func.now())
    updated_time = db.Column(db.DateTime)

    # tc = db.relationship('TimeCard', primaryjoin='TimeCardMemo.tc_id == TimeCard.tc_id', backref='time_card_memos')


class Weekly(db.Model):
    __tablename__ = 'Weekly'

    weekly_id = db.Column(db.Integer, primary_key=True)
    wcond_id = db.Column(db.ForeignKey('WorkCondition.wcond_id'), nullable=False, index=True)
    created_time = db.Column(db.DateTime, server_default=func.now())
    updated_time = db.Column(db.DateTime)

    wcond = db.relationship('WorkCondition', primaryjoin='Weekly.wcond_id == WorkCondition.wcond_id', backref='weeklies')


class WorkCondition(db.Model):
    __tablename__ = 'WorkCondition'

    wcond_id = db.Column(db.Integer, primary_key=True, nullable=False)
    cont_id = db.Column(db.ForeignKey('WorkContract.cont_id', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    user_id = db.Column(db.Integer, nullable=False, index=True)
    wp_id = db.Column(db.Integer, nullable=False)
    work_date = db.Column(db.String(8), primary_key=True, nullable=False)
    week_num = db.Column(db.Integer)
    day_num = db.Column(db.Integer)
    start_work_time = db.Column(db.Time)
    end_work_time = db.Column(db.Time)
    amount_work_time = db.Column(db.Time)
    amount_rest_time = db.Column(db.Time)
    hourly_pay = db.Column(db.Numeric(12, 2))
    daily_pay = db.Column(db.Numeric(12, 2))
    wcond_status = db.Column(db.Integer, nullable=False, server_default='1')
    created_time = db.Column(db.DateTime, server_default=func.now())
    updated_time = db.Column(db.DateTime)

    cont = db.relationship('WorkContract', primaryjoin='WorkCondition.cont_id == WorkContract.cont_id', backref='work_conditions')


class WorkContract(db.Model):
    __tablename__ = 'WorkContract'

    cont_id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.ForeignKey('User.user_id'), nullable=False, index=True)
    wp_id = db.Column(db.ForeignKey('WorkPlace.wp_id'), nullable=False, index=True)
    cont_date = db.Column(db.String(8), primary_key=True, nullable=False)
    first_start_date = db.Column(db.String(8))
    _1_start_pot = db.Column('1_start_pot', db.Time)
    _1_end_pot = db.Column('1_end_pot', db.Time)
    _1_rest_aot = db.Column('1_rest_aot', db.Time)
    _2_start_pot = db.Column('2_start_pot', db.Time)
    _2_end_pot = db.Column('2_end_pot', db.Time)
    _2_rest_aot = db.Column('2_rest_aot', db.Time)
    _3_start_pot = db.Column('3_start_pot', db.Time)
    _3_end_pot = db.Column('3_end_pot', db.Time)
    _3_rest_aot = db.Column('3_rest_aot', db.Time)
    _4_start_pot = db.Column('4_start_pot', db.Time)
    _4_end_pot = db.Column('4_end_pot', db.Time)
    _4_rest_aot = db.Column('4_rest_aot', db.Time)
    _5_start_pot = db.Column('5_start_pot', db.Time)
    _5_end_pot = db.Column('5_end_pot', db.Time)
    _5_rest_aot = db.Column('5_rest_aot', db.Time)
    _6_start_pot = db.Column('6_start_pot', db.Time)
    _6_end_pot = db.Column('6_end_pot', db.Time)
    _6_rest_aot = db.Column('6_rest_aot', db.Time)
    _7_start_pot = db.Column('7_start_pot', db.Time)
    _7_end_pot = db.Column('7_end_pot', db.Time)
    _7_rest_aot = db.Column('7_rest_aot', db.Time)
    week_holiday = db.Column(db.Integer)
    work_day_cnt = db.Column(db.Integer)
    hourly_pay = db.Column(db.Numeric(12, 2))
    monthly_pay = db.Column(db.Numeric(12, 2))
    pay_init_day = db.Column(db.Integer, server_default='1')
    pay_day = db.Column(db.Integer, server_default='10')
    work_time_offset = db.Column(db.Time, server_default='00:05:00')
    having_photo = db.Column(db.String(255))
    cont_status = db.Column(db.Integer, nullable=False, server_default='1')
    created_time = db.Column(db.DateTime, server_default=func.now())
    updated_time = db.Column(db.DateTime)

    user = db.relationship('User', primaryjoin='WorkContract.user_id == User.user_id', backref='work_contracts')
    wp = db.relationship('WorkPlace', primaryjoin='WorkContract.wp_id == WorkPlace.wp_id', backref='work_contracts')


class WorkPlace(db.Model):
    __tablename__ = 'WorkPlace'

    wp_id = db.Column(db.Integer, primary_key=True)
    wp_name = db.Column(db.String(45))
    address = db.Column(db.String(255))
    kakao_place_id = db.Column(db.String(45))
    road_address = db.Column(db.String(255))
    category_name = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    bjd_code = db.Column(db.String(10))
    building_name = db.Column(db.String(255))
    business_code = db.Column(db.String(45))
    owner = db.Column(db.String(45))
    over_5employee = db.Column(db.Integer, server_default='1')
    x = db.Column(db.Text)
    y = db.Column(db.Text)
    created_time = db.Column(db.DateTime, server_default=func.now())
    updated_time = db.Column(db.DateTime)


class Yearly(db.Model):
    __tablename__ = 'Yearly'

    yearly_id = db.Column(db.Integer, primary_key=True)
    wcond_id = db.Column(db.ForeignKey('WorkCondition.wcond_id'), nullable=False, index=True)
    created_time = db.Column(db.DateTime, server_default=func.now())
    updated_time = db.Column(db.DateTime)

    wcond = db.relationship('WorkCondition', primaryjoin='Yearly.wcond_id == WorkCondition.wcond_id', backref='yearlies')


