from flask import Blueprint

task_page = Blueprint('tasks', __name__, url_prefix='/task')

from tasks.view import *
