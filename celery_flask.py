from flask import (
    Flask,
    request,
    render_template,
    jsonify,
    url_for
)
from celery_configuration import make_celery
import time

flask_app = Flask(__name__)
flask_app.config.from_object('settings')
celery = make_celery(flask_app)


@celery.task(name="celery task")
def sleep(_time, name):
    time.sleep(_time)
    return name


@flask_app.route("/time_sleep/", methods=["GET", "POST"])
def hello():
    params = request.get_json(force=True)
    time = params.get("time")
    name = params.get("name")
    sleep.delay(time, name)
    message = "sleep for {sleep_time} seconds".format(sleep_time=time)
    return {"name": name, "message": message}


if __name__ == "__main__":
    flask_app.run()