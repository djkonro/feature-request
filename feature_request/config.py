class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://test:testing@localhost/testdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class DockerDeployConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://test:testing@mysql/testdb'

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tests/db.tests'
    TESTING = True
