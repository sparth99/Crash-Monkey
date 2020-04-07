from models import db

class Logs(db.Model):
    __tablename__ == "Logs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String(), nullable=False, unique=False)
    text = db.Column(db.String(), nullable=False, unique=False)

