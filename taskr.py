from flask import Flask
from user import page as user_bp
from tasks import task_page as task_bp
from database.manager import db, initialized

app = Flask(__name__)

# set configurations
app.config.from_pyfile('configs.py')

# init components (database, logger, triggers ...)
from tasks.model import *
db.init_app(app)
db.create_all(app=app)

# import all models

# register all blueprints
app.register_blueprint(user_bp)
app.register_blueprint(task_bp)


@app.route('/')
def hello():
    return 'Hello, welcome to the taskr Api 1.0'


if __name__ == '__main__':
    app.run()
