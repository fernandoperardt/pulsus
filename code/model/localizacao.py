from app import db

class LocalizacaoModel(db.Model):
    __tablename__ = 'localizacao'

    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))
    latitude = db.Column(db.Float(precision=8))
    longitude = db.Column(db.Float(precision=8))
    data = db.Column(db.DateTime)

    def json(self):
        return {'latitude': self.latitude, 'longitude': self.longitude}

    def __init__(self, device_id, latitude, longitude, data) -> None:
        self.device_id = device_id
        self.latitude = latitude
        self.longitude = longitude
        self.data = data

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
