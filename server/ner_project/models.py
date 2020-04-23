from datetime import datetime
from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    projects = db.relationship('Project', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)
    summary = db.Column(db.String(128), index=True)
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    entity_classes = db.relationship(
        'EntityClass', backref='project', lazy='dynamic')

    @property
    def as_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "summary": self.summary,
            "created": self.created.isoformat()
        }

    def __repr__(self):
        return '<Project {}>'.format(self.name)


class EntityClass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    @property
    def as_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "project_id": self.project_id,
            "created": self.created.isoformat()
        }

    def __repr__(self):
        return '<EntityClass {}>'.format(self.name)
