from flask import Blueprint, request, jsonify
from database.models import Sensor, SensorData  # database 폴더에서 정의된 모델을 import

sensor_routes = Blueprint('sensor_routes', __name__)


@sensor_routes.route('/data', methods=['POST'])
def add_sensor_data():
    data = request.json
    new_data = SensorData(sensor_id=data['sensor_id'], value=data['value'])
    # DB에 저장하는 코드
    return jsonify({"message": "Data added"}), 201


@sensor_routes.route('/data/<int:sensor_id>', methods=['GET'])
def get_sensor_data(sensor_id):
    data = SensorData.query.filter_by(sensor_id=sensor_id).all()
    # 반환 형태를 맞춰서 jsonify로 반환
    return jsonify({"data": data}), 200
