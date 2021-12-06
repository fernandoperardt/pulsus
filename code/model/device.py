from app import db
from model.nome import NomeModel
from datetime import datetime

class DeviceModel(db.Model):
    __tablename__ = 'device'

    id = db.Column(db.Integer, primary_key=True)
    deviceid = db.Column(db.String)
    data = db.Column(db.DateTime)
    localizacao = db.relationship('LocalizacaoModel', backref='localizacao', lazy=True)
    nome = db.relationship('NomeModel', backref='nomeModel', lazy=True)


    def __init__(self, deviceid, data) -> None:
        self.deviceid = deviceid
        self.data = data

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        return self.id


    def json(self):
        return {'deviceid': self.deviceid, 'nome': [nome.json() for nome in self.nome], 'localizacao': [loc.json() for loc in self.localizacao], 'data': self.data.__str__()}

    @classmethod
    def getAll(cls):
        return cls.query.all()

    @classmethod
    def geByDeviceId(cls, deviceid):
        return cls.query.filter_by(deviceid = deviceid).all()

    @classmethod
    def geByDeviceIdAndData(cls, deviceid, data_inicio, data_fim):
        return cls.query.filter(cls.deviceid == deviceid, cls.data >= data_inicio, cls.data <= data_fim).all()