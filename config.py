import os

class Config:
    '''
    General configuration parent class
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql://dhovgbzfvxunxq:1f91713e33aaea07cbeaa552d7744024a163014915a875621d31fdface5244fa@ec2-54-164-40-66.compute-1.amazonaws.com:5432/d7mvbcpmgju4cj'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # UPLOADED_PHOTOS_DEST ='app/static/photos'
    # #  email configurations
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # # simple mde  configurations
    # SIMPLEMDE_JS_IIFE = True
    # SIMPLEMDE_USE_CDN = True
    # @staticmethod
    # def init_app(app):
    pass

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql://dhovgbzfvxunxq:1f91713e33aaea07cbeaa552d7744024a163014915a875621d31fdface5244fa@ec2-54-164-40-66.compute-1.amazonaws.com:5432/d7mvbcpmgju4cj'
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql://dhovgbzfvxunxq:1f91713e33aaea07cbeaa552d7744024a163014915a875621d31fdface5244fa@ec2-54-164-40-66.compute-1.amazonaws.com:5432/d7mvbcpmgju4cj'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}

