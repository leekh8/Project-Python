from flask import Blueprint, request, jsonify
from database.models import User  # database 폴더에서 정의된 User 모델을 import
from werkzeug.security import generate_password_hash, check_password_hash

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(email=data['email'], password=hashed_password)
    # DB에 저장하는 코드
    return jsonify({"message": "User created"}), 201


@user_routes.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        # 토큰 생성 및 반환
        return jsonify({"message": "Logged in"}), 200
    else:
        return jsonify({"message": "Bad credentials"}), 401
