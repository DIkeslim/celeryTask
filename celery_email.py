from flask import (
    Flask,
    request,
    render_template,
    jsonify,
    url_for
)
from flask_mail import Mail, Message
from celery_configuration import make_celery
import time

flask_app = Flask(__name__)
flask_app.config.from_object('settings')
mail = Mail(flask_app)
celery = make_celery(flask_app)


@celery.task(name="Email Sender")
def mail_sender(receiver, username):
    email_data = {
        "subject": "Happy to join us, {}".format(username),
        "to": receiver,
        "body": "Welcome to jon us!"
    }
    msg = Message(
        email_data["subject"],
        sender = flask_app.config["MAIL_DEFAULT_SENDER"],
        recipients = [email_data["to"]]
    )
    msg.body = email_data['body']
    with flask_app.app_context():
        mail.send(msg)


@flask_app.route("/send/mail/", methods=["GET", "POST"])
def send_email():
    params = request.get_json()
    receiver = params.get("receiver")
    username = params.get("username")
    mail_sender.delay(receiver, username)
    return "Hello, {}. Confirm mail sent already, please check your mailbox.".format(username)




if __name__ == "__main__":
    flask_app.run()