from database.manager import get_db_session
from .model import TaskBoard, Task
from util.ErrorCodes import *


def get_task_board_by_id(taskboard_id, json=False):
    with get_db_session(commit=False) as session:
        result = session.query(TaskBoard).filter(TaskBoard.id.is_(taskboard_id)).first()

    if result is None:
        return create_error_message(TASKBOARD_DOES_NOT_EXIST)
    if json:
        return result.serialize()
    return result


def create_task_board(**kwargs):
    t = TaskBoard(**kwargs)
    with get_db_session() as session:
        session.add(t)
    return t.serialize()


# BUG: creates a Response object which is not Serializable.. -_-
def get_all_taskboards():
    data = TaskBoard.query.all()
    print(data)
    result = []
    for board in data:
        task = board
        result.append(task.serialize())
    print(result)
    return jsonify(result)


def get_taskboard_by_public_id(public_id, json=False):
    with get_db_session(commit=False) as session:
        result = session.query(TaskBoard).filter(TaskBoard.public_id.is_(public_id)).first()
    if result is None:
        return jsonify(create_error_message(TASKBOARD_DOES_NOT_EXIST))
    if json:
        return jsonify(result.serialize())
    return result


def create_task(taskboard, **kwargs):
    from flask import jsonify
    board = get_task_board_by_id(taskboard)
    if board is None:
        return create_error_message(TASKBOARD_DOES_NOT_EXIST)
    if len(board.tasks.all()) >= board.max_tasks:
        return jsonify(create_error_message(TASKBOARD_IS_FULL))
    task = Task(**kwargs)
    with get_db_session() as session:
        session.add(task)
    return jsonify(task.serialize())


def delete_task_by_id(*args):
    with get_db_session(commit=True) as session:
        for task_id in args:
            task = session.query(Task).filter(Task.id.is_(task_id)).first()
            session.delete(task)

    return 'Deleted {}'.format(args)
