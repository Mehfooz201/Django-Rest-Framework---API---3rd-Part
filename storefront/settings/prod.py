import os
from .common import *


DEBUG = False

SECRET_KEY = "3t3#fiy(37@vnbb!@^zq15-u1___q7!%gob55!h0-(gra8=#wl"
# os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['mehfooz-prod-923f62a54d1a.herokuapp.com']


EMAIL_HOST = os.environ['MAILGUN_SMTP_SERVER']
EMAIL_HOST_USER = os.environ['MAILGUN_SMTP_LOGIN']
EMAIL_HOST_PASSWORD = os.environ['MAILGUN_SMTP_PASSWORD']
EMAIL_PORT = os.environ['MAILGUN_SMTP_PORT']
# DEFAULT_FROM_EMAIL = 'from@mehfoozpy.com'
