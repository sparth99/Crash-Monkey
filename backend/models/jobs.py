from models import db

class Jobs(db.Model):
    __tablename__ == "Jobs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_time = db.Column(db.String(), nullable=False, unique=False)
    end_time = db.Column(db.String(), nullable=False, unique=True)
    stress_test = db.Column(db.String(), nullable=False, unique=False)