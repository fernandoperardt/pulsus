from flask_restful import Resource, reqparse, request
from model.nome import NomeModel
from model.device import DeviceModel
from model.localizacao import LocalizacaoModel
from datetime import datetime

class Device(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('deviceid',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    parser.add_argument('nome',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    parser.add_argument('latitude',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    parser.add_argument('longitude',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    def post(self, deviceid = None, data = None):
        print('to aqui')
        data =  Device.parser.parse_args()
        data_agora = datetime.now()
        device = DeviceModel(data['deviceid'], data_agora)
        device_id = device.save_to_db()
        if device_id is None:
            return 500
        nome = NomeModel(device_id, data['nome'], data_agora)
        localizacao = LocalizacaoModel(device_id, data['latitude'], data['longitude'], data_agora)        

        nome.save_to_db()
        localizacao.save_to_db()

    def get(self, deviceid = None):
        if deviceid:
            request_data = request.args
            if 'ddMMyyyyhhmm' in request_data:
                data_filtro = request_data['ddMMyyyyhhmm']
                try:
                    data_inicio = datetime.strptime(data_filtro + '00', '%d%m%Y%H%M%S')
                    data_fim = datetime.strptime(data_filtro + '59', '%d%m%Y%H%M%S')
                    return {'devices': [device.json() for device in DeviceModel.geByDeviceIdAndData(deviceid, data_inicio, data_fim)]}, 201
                except:
                    return None, 500
            else:
                return {'devices': [device.json() for device in DeviceModel.geByDeviceId(deviceid)]}, 201

        return {'devices': [device.json() for device in DeviceModel.getAll()]}, 201