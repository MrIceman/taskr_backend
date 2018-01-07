from database.manager import db

forbidden_chars = ['<', '>', '#', '_', 'metadata', ]


class AbstractDbModel():
    methods = []

    def __init__(self, **kwargs):
        # everything that should be ignored when serializing / deserializing
        self.methods.append('serialize')
        self.methods.append('deserialize')
        self.methods.append('methods')

        for key, value in kwargs.items():
            if key in self.__dir__():
                self.__setattr__(key, value)
        # setting custom flags, which determine if any additional attributes should be ignored
        if 'flags' in kwargs:
            for flag in kwargs['flags']:
                self.methods.append(flag)


class TaskBoard(AbstractDbModel, db.Model):
    __tablename__ = 'taskboard'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, default='No Title')
    description = db.Column(db.Text, default='No Description')
    secret = db.Column(db.Text, default='cheese')
    public_id = db.Column(db.Text)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    last_update = db.Column(db.DateTime, server_onupdate=db.func.now())
    tasks = db.relationship('Task', backref='taskboard', lazy='dynamic')
    max_tasks = db.Column(db.Integer, default=8)

    def serialize(self):
        print('Serializing..')
        from flask import jsonify
        result = dict()
        result['id'] = self.id
        result['title'] = self.title
        result['description'] = self.description
        result['secret'] = self.secret
        result['public_id'] = self.public_id
        result['created_on'] = self.created_on
        result['max_tasks'] = self.max_tasks
        result['last_update'] = self.last_update
        return jsonify(result)


class Task(AbstractDbModel, db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, default='No Title')
    content = db.Column(db.Text, default='No Content yet')
    taskboard_id = db.Column(db.Integer, db.ForeignKey(column='taskboard.id', name='taskboard'))
