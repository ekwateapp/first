import os

class BaseConfig(object):
    pass

class DebugConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SECRET_KEY = 's(kp3Ue8feLuNfhy!L5&0XGMhFk6^65XgF3))Ix4MD#ilz(n7uPaaTEogjb@BDTf'

class ProductionConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True    
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql+psycopg2://postgres:P@55word@localhost/vfcake2015')
    SECRET_KEY = 's(kp3Ue8feLuNfhy!L5&0XGMhFk6^65XgF3))Ix4MD#ilz(n7uPaaTEogjb@BDTf'