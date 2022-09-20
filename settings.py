import os

import gmail as gmail

CELERY_BROKER_URL='redis://localhost:6379/0'
CELERY_RESULT_BACKEND='redis://localhost:6379/0'


#https://myaccount.google.com/lesssecureapps
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = "yourEmail@gmail.com"
MAIL_PASSWORD = 'yourPassword'
MAIL_DEFAULT_SENDER = "yourEmail@gmail.com"