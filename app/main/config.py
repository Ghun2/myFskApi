import os, sys
sys.path.insert(0, '/opt/drslr/app_config'); import config

basedir = os.path.abspath(os.path.dirname(__file__))

DB_NAME = 'DRSLR_V7'

TB_DB_URL = 'mysql+mysqldb://{}:{}@{}:3306/{}?charset=utf8mb4'.format(
    config.Config.LOCAL_DB["user"],
    config.Config.LOCAL_DB["password"],
    config.Config.LOCAL_DB["host"],
    DB_NAME
)

PRD_DB_URL = 'mysql+mysqldb://{}:{}@{}:3306/{}?charset=utf8mb4'.format(
    config.Config.REMOTE_DB["user"],
    config.Config.REMOTE_DB["password"],
    config.Config.REMOTE_DB["host"],
    DB_NAME
)

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'rest_api_drsalary')
    DEBUG = False


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = TB_DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = TB_DB_URL
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    SQLALCHEMY_DATABASE_URI = PRD_DB_URL


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
