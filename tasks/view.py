from tasks import task_page
from flask import request
from util.ErrorCodes import *
from tasks.operator import get_taskboard_by_public_id, \
    get_task_board_by_id, create_task_board, get_all_taskboards, create_task, delete_task_by_id


@task_page.route('/taskboard/get/', methods=['POST', 'GET'])
def get_board():
    if request.method == 'GET':
        return 'Only post requests are valid'
    data = request.json
    if 'public_id' in data:
        result = get_taskboard_by_public_id(data['public_id'], json=True)
        return result
    elif 'id' in data:
        id = data['id']
        return get_task_board_by_id(id, json=True)
    return 'Wrong Keys. Received: {}'.format(data)


@task_page.route('/taskboard/get/all')
def get_all_boards():
    return get_all_taskboards()


@task_page.route('/taskboard/create/', methods=['POST'])
def make_taskboard():
    required_keys = ['secret', ]
    data = request.json
    for key in required_keys:
        if key not in data:
            return jsonify(create_error_message(MISSING_PARAMS))
    if 'id' in data:
        return 'You can not set your own ID, dude!'
    taskboard_data = {x: y for x, y in data.items()}
    return create_task_board(**taskboard_data)


@task_page.route('/create/', methods=['POST'])
def make_task():
    required_keys = ['taskboard_id']
    data = request.json
    for key in required_keys:
        if key not in data:
            return jsonify(create_error_message(MISSING_PARAMS))
    if 'id' in data:
        return 'You can not set your own ID, dude!'
    task_data = {x: y for x, y in data.items()}
    return create_task(data['taskboard_id'], **task_data)


@task_page.route('/delete/', methods=['POST'])
def delete_task():
    data = request.json
    if 'ids' not in data:
        return create_error_message(MISSING_PARAMS)
    return delete_task_by_id(*data['ids'])