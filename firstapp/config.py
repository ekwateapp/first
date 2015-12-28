class BaseConfig(object):
    pass

class DebugConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SECRET_KEY = 's(kp3Ue8feLuNfhy!L5&0XGMhFk6^65XgF3))Ix4MD#ilz(n7uPaaTEogjb@BDTf'