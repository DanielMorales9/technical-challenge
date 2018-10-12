class Config(object):
    DEBUG = False
    TESTING = False
    crashed = False


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    failure_rate = 0.2
