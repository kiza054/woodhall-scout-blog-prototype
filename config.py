import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'thisisasecret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'blog_data.db')
    #'mysql://username:password@server/db'
    MAIL_SERVER = 'smtp.mail.yahoo.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_SSL') is not None or 1
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'k.sarda_1stWoodhall.yahoo.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'ksarda_1stwoodhall'
    ADMINS = ['k.sarda_1stWoodhall.yahoo.com']
    FLASK_ADMIN_SWATCH = 'cyborg'
    POSTS_PER_PAGE = 25
    BABEL_DEFAULT_LOCALE = 'en'
    LANGUAGES = ['en', 'fr', 'es', 'pl', 'ar', 'pa', 'hi']
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL') or 'http://127.0.0.1:9200'
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY') or 'feeec6e7b57548678b0fef5991282e33'
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    #UPLOAD_FOLDER = '/home/ubuntu/nea_project/app/static/uploads/'