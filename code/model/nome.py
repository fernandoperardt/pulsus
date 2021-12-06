from app import db

class NomeModel(db.Model):
    __tablename__ = 'nome'

    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))
    nome = db.Column(db.String(80))
    data = db.Column(db.DateTime)


    def __init__(self, device_id, nome, data) -> None:
        self.device_id = device_id
        self.nome = nome
        self.data = data

    def json(self):
        return {'nome': self.nome}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()