from os import getenv

class Config(object):
    DEBUG = False
    SECRET_KEY = '### please-override-in-production ###'
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ('mariadb+mariadbconnector://'
                              f'{getenv("SYNCEDIT_DBUSER")}'
                              f':{getenv("SYNCEDIT_DBPASS")}'
                              f'@{getenv("SYNCEDIT_DBHOST")}'
                              f':{getenv("SYNCEDIT_DBPORT")}'
                              f'/{getenv("SYNCEDIT_DBNAME")}')
