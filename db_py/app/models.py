from app import app, db


class VehicleRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gate = db.Column(db.String(255), nullable=True)
    year = db.Column(db.String(255), nullable=True)
    month = db.Column(db.String(255), nullable=True)
    hour = db.Column(db.String(255), nullable=True)
    day = db.Column(db.String(255), nullable=True)
    no_veh = db.Column(db.String(255), nullable=True)

    def __init__(self, gate, year, hour, day, no_veh):
        self.gate = gate
        self.year = year
        self.hour = hour
        self.day = day
        self.no_veh = no_veh
