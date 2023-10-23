from sqlalchemy import Column, Integer, String, DateTime, Text, Float, ForeignKey
from sqlalchemy.orm import relationship
from connection import db


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    date_joined = Column(DateTime, default="CURRENT_TIMESTAMP")

    sensors = relationship("Sensor", backref="user")


class Sensor(db.Model):
    __tablename__ = 'sensors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    name = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)
    location = Column(String(255), nullable=True)

    sensor_data = relationship("SensorData", backref="sensor")


class SensorData(db.Model):
    __tablename__ = 'sensor_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sensor_id = Column(Integer, ForeignKey('sensors.id'), nullable=True)
    timestamp = Column(DateTime, default="CURRENT_TIMESTAMP")
    value = Column(Float, nullable=False)


class FishData(db.Model):
    __tablename__ = 'fish_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)


class PlantData(db.Model):
    __tablename__ = 'plant_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
