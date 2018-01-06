from tasks import task_page
from flask import request
from tasks.operator import get_task_board_by_id, create_task_board, get_all_taskboards


@task_page.route('/taskboard/get/', methods=['POST', 'GET'])
def get_board():
    if request.method == 'GET':
        return 'Only post requests are valid'

    data = request.json
    id = data['id']
    return get_task_board_by_id(id, json=True)


@task_page.route('/taskboard/get/all')
def get_all_boards():
    return get_all_taskboards()


@task_page.route('/taskboard/create/', methods=['POST'])
def create_task():
    data = request.json
    if 'id' in data:
        return 'You can not set your own ID, dude!'
    task_data = {x: y for x, y in data.items()}
    return create_task_board(**task_data)