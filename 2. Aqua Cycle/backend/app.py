from flask import Flask
from database.models import db  # models.py에서 정의된 db 객체 import
from routes.main_routes import app as main_routes
from routes.user_routes import user_routes
from routes.sensor_routes import sensor_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = YOUR_DATABASE_URI_FROM_CONFIG

db.init_app(app)

app.register_blueprint(main_routes)
app.register_blueprint(user_routes, url_prefix='/user')
app.register_blueprint(sensor_routes, url_prefix='/sensor')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000, debug=True)
