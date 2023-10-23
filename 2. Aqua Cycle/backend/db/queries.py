from connection import db
from models import User, Sensor, SensorData, FishData, PlantData

# Create


def create_user(username, password, email):
    new_user = User(username=username, password=password, email=email)
    db.session.add(new_user)
    db.session.commit()
    return new_user


def create_sensor(user_id, name, sensor_type, location):
    new_sensor = Sensor(user_id=user_id, name=name,
                        type=sensor_type, location=location)
    db.session.add(new_sensor)
    db.session.commit()
    return new_sensor


def create_fish_data(name, description):
    new_fish_data = FishData(name=name, description=description)
    db.session.add(new_fish_data)
    db.session.commit()
    return new_fish_data


def create_plant_data(name, description):
    new_plant_data = PlantData(name=name, description=description)
    db.session.add(new_plant_data)
    db.session.commit()
    return new_plant_data

# Read


def get_user_by_username(username):
    user = User.query.filter_by(username=username).first()
    return user


def get_sensors_by_user_id(user_id):
    sensors = Sensor.query.filter_by(user_id=user_id).all()
    return sensors


def get_fish_data_by_name(name):
    fish_data = FishData.query.filter_by(name=name).first()
    return fish_data


def get_plant_data_by_name(name):
    plant_data = PlantData.query.filter_by(name=name).first()
    return plant_data

# Update


def update_user_email(user_id, new_email):
    user = User.query.get(user_id)
    if user:
        user.email = new_email
        db.session.commit()
        return user
    return None


def update_sensor_name(sensor_id, new_name):
    sensor = Sensor.query.get(sensor_id)
    if sensor:
        sensor.name = new_name
        db.session.commit()
        return sensor
    return None


def update_fish_data(fish_id, new_name, new_description):
    fish_data = FishData.query.get(fish_id)
    if fish_data:
        fish_data.name = new_name
        fish_data.description = new_description
        db.session.commit()
        return fish_data
    return None


def update_plant_data(plant_id, new_name, new_description):
    plant_data = PlantData.query.get(plant_id)
    if plant_data:
        plant_data.name = new_name
        plant_data.description = new_description
        db.session.commit()
        return plant_data
    return None

# Delete


def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False


def delete_sensor(sensor_id):
    sensor = Sensor.query.get(sensor_id)
    if sensor:
        db.session.delete(sensor)
        db.session.commit()
        return True
    return False


def delete_fish_data(fish_id):
    fish_data = FishData.query.get(fish_id)
    if fish_data:
        db.session.delete(fish_data)
        db.session.commit()
        return True
    return False


def delete_plant_data(plant_id):
    plant_data = PlantData.query.get(plant_id)
    if plant_data:
        db.session.delete(plant_data)
        db.session.commit()
        return True
    return False
