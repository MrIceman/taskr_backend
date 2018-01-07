from flask import jsonify

ERROR_PREFIX = 'error'
ERROR_CODE_PREFIX = 'code'
TASKBOARD_DOES_NOT_EXIST = 100
TASKBOARD_IS_FULL = 101
WRONG_PARAMS = 102
MISSING_PARAMS = 103


def create_error_message(error_code):
    return {ERROR_PREFIX: {ERROR_CODE_PREFIX: error_code}}
