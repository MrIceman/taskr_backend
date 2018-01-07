from database.manager import db

forbidden_chars = ['<', '>', '#', '_', 'metadata', ]


class AbstractDbModel:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.__dir__():
                self.__setattr__(key, value)


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
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'secret': self.secret,
            'public_id': self.public_id,
            'created_on': self.created_on,
            'max_tasks': self.max_tasks,
            'last_update': self.last_update,
            'tasks': [item.serialize() for item in self.tasks]
        }


class Task(AbstractDbModel, db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, default='No Title')
    content = db.Column(db.Text, default='No Content yet')
    author = db.Column(db.Text, nullable=False, default='Anon')
    date = db.Column(db.DateTime, default=db.func.now())
    taskboard_id = db.Column(db.Integer, db.ForeignKey(column='taskboard.id', name='taskboard'))

    def serialize(self):
        print('Serializing..')
        result = dict()
        result['id'] = self.id
        result['title'] = self.title
        result['content'] = self.content
        result['author'] = self.author
        result['date'] = self.date
        result['taskboard_id'] = self.taskboard_id
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'date': self.date,
            'taskboard_id': self.taskboard_id,
        }
