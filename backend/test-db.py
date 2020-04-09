import sys
sys.path.append('../backend/models/')
from models import db, Jobs

db.session.add(
    Jobs(
        start_time = str("0"),
        end_time = str("0"),
        stress_test = str("0"),
    )
)