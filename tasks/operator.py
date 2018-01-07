from database.manager import get_db_session
from .model import TaskBoard, Task
from flask import jsonify


def get_task_board_by_id(taskboard_id, json=False):
    with get_db_session(commit=False) as session:
        result = session.query(TaskBoard).filter(TaskBoard.id.is_(taskboard_id)).first()

    if result is None:
        return 'No TaskBoard with id {} found'.format(taskboard_id)
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
        return 'No TaskBoard with public id {} found'.format(public_id)
    if json:
        return result.serialize()
    return result
