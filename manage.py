import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app import blueprint
from app.main import create_app, db
from app.main.model.user import User
from app.main.model import b_logic
from constants.local_run import RUN_SETTING, TB_RUN_SETTING


# app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
# app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app = create_app('dev')

app.config['FLASK_ADMIN_SWATCH'] = 'superhero'

admin = Admin(app, name='닥터샐러리 관리자', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(b_logic.WorkPlace, db.session))
admin.add_view(ModelView(b_logic.WorkContract, db.session))
admin.add_view(ModelView(b_logic.WorkCondition, db.session))
admin.add_view(ModelView(b_logic.TimeCard, db.session))
admin.add_view(ModelView(b_logic.TimeCardMemo, db.session))
admin.add_view(ModelView(b_logic.Daily, db.session))
admin.add_view(ModelView(b_logic.Weekly, db.session))
admin.add_view(ModelView(b_logic.Monthly, db.session))
admin.add_view(ModelView(b_logic.Yearly, db.session))
admin.add_view(ModelView(b_logic.CategoryLaw, db.session))
admin.add_view(ModelView(b_logic.IncomeTax, db.session))
admin.add_view(ModelView(b_logic.TermsAgreement, db.session))
admin.add_view(ModelView(b_logic.FAQ, db.session))

# admin.add_view(ModelView(B_logic, db.session))

app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(**TB_RUN_SETTING)


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__' :
    manager.run()

