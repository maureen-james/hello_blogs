import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgres://sbhziyzvmhgamd:ce20a651d13d46cc502481f5082a46ced7b97fcb6b00ee9792dbafa24905be5f@ec2-52-3-2-245.compute-1.amazonaws.com:5432/da0jkctgn0psl7'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    @staticmethod
    def init_app(app):
     pass

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://sbhziyzvmhgamd:ce20a651d13d46cc502481f5082a46ced7b97fcb6b00ee9792dbafa24905be5f@ec2-52-3-2-245.compute-1.amazonaws.com:5432/da0jkctgn0psl7'
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgres://sbhziyzvmhgamd:ce20a651d13d46cc502481f5082a46ced7b97fcb6b00ee9792dbafa24905be5f@ec2-52-3-2-245.compute-1.amazonaws.com:5432/da0jkctgn0psl7'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}

