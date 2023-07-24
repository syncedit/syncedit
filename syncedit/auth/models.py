from syncedit.extensions import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password, email) -> None:
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self) -> str:
        return f'<User {self.username}>'
