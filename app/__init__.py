import logging, os
from config import Config
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_admin import Admin
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel, lazy_gettext as _l

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)
login = LoginManager(app)
login.login_view = 'auth.login'
login.login_message = _l('Please log in to access this page')
bootstrap = Bootstrap(app)
mail = Mail(app)
moment = Moment(app)
babel = Babel(app)

from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)

from app.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')

from app.main import bp as main_bp
app.register_blueprint(main_bp)

from app import models
from app.auth.admin import AdminView
from flask_admin.menu import MenuLink
from flask_admin.contrib.sqla import ModelView
from app.models import User, Post, Message, Notification

admin = Admin(app, name='1st Woodhall Blog\'s Admin Dashboard', template_mode='bootstrap3', index_view=AdminView(User,
                                                            db.session, url='/admin', endpoint='admin'))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Message, db.session))
admin.add_view(ModelView(Notification, db.session))
admin.add_link(MenuLink(name='Back to Homepage', category='', url='/'))

if not os.path.exists('logs'):
    os.mkdir('logs')
file_handler = RotatingFileHandler('logs/1st_woodhall_blog.log', maxBytes=10240, backupCount=20)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

app.logger.setLevel(logging.INFO)
app.logger.info('1st Woodhall Blog Startup')

if app.config['LOG_TO_STDOUT']:
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    app.logger.addHandler(stream_handler)
else:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/1st_woodhall_blog.log',
                                       maxBytes=10240, backupCount=20)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('1st Woodhall Blog Startup')

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])