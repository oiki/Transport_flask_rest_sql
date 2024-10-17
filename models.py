
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Transport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    transport_type = db.Column(db.String(50), nullable=False)
    transport_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Transport {self.patient_name} - {self.transport_type}>'
