import os


folder = os.path.dirname(os.path.abspath(__file__))



class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(24)

class ProductionConfig(Config):
    DEBUG = False
    DB_FILE = os.path.join(folder,"ifkdb.sqlite")

class StagingConfig(Config):
    DEBUG = True
    DB_FILE = os.path.join(folder,"ifkdb.sqlite")

class DevelopmentConfig(Config):
    DB_FILE = os.path.join(folder, "ifkdb.sqlite")
    try:
        os.remove(DB_FILE)
    except:
        pass

    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DB_FILE = ":memory:"