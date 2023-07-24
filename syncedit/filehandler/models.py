from syncedit.extensions import db
from datetime import datetime

class File(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    size = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    modified = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, name, owner, content='') -> None:
        self.name = name
        self.owner = owner
        self.content = content
        self.size = len(content)

    def __repr__(self) -> str:
        return f'<File {self.name}>'


class Folder(db.Model):
    __tablename__ = 'folders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    items = db.Column(db.Integer, nullable=False, default=0)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    accessed = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f'<Folder {self.name}>'

