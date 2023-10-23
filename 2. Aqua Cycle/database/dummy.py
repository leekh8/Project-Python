import pymysql as ps
from faker import Faker
import random

# 데이터베이스 연결
conn = ps.connect(user='admin', password='admin', database='aquacycle')

cursor = conn.cursor()

# Faker 인스턴스 생성
fake = Faker()


# 사용자 더미 데이터 생성 및 삽입
for _ in range(100):
    email = fake.email()
    password = fake.password()
    query = "INSERT INTO Users (email, password) VALUES (%s, %s);"
    cursor.execute(query, (email, password))

# 아쿠아포닉스 시스템 더미 데이터
for _ in range(100):
    user_id = random.randint(1, 100)
    name = fake.company()
    cursor.execute(
        "INSERT INTO Systems (user_id, name) VALUES (%s, %s);", (user_id, name))

# 센서 유형 더미 데이터 추가
sensor_types = ['Temperature', 'Humidity',
                'Water Temperature', 'Water Level', 'Water Quality']
for sensor in sensor_types:
    cursor.execute(
        "INSERT INTO SensorTypes (type_name) VALUES (%s);", [sensor])

# 센서 더미 추가
for _ in range(500):
    system_id = random.randint(1, 100)
    sensor_type_id = random.randint(1, 5)  # Assuming 5 sensor types
    cursor.execute("INSERT INTO Sensors (system_id, sensor_type_id) VALUES (%s, %s);",
                   (system_id, sensor_type_id))

# 센서 데이터 더미 데이터
for _ in range(1000):
    sensor_id = random.randint(1, 500)
    value = random.uniform(0, 100)
    cursor.execute(
        "INSERT INTO SensorData (sensor_id, value) VALUES (%s, %s);", (sensor_id, value))

# 물고기 데이터 더미 추가
fishes = ['Goldfish', 'Betta', 'Guppy', 'Molly', 'Platy',
          'Angelfish', 'Neon Tetra', 'Oscar', 'Zebrafish', 'Mantis Shrimp']
for fish in fishes:
    max_temp = random.uniform(20, 30)
    min_temp = random.uniform(10, 20)
    max_quality = random.uniform(7, 9)
    min_quality = random.uniform(5, 7)
    description = fake.sentence()
    cursor.execute("INSERT INTO FishInfo (name, max_optimal_temperature, min_optimal_temperature, max_optimal_water_quality, min_optimal_water_quality, description) VALUES (%s, %s, %s, %s, %s, %s);",
                   (fish, max_temp, min_temp, max_quality, min_quality, description))

# 식물 데이터 더미 추가
plants = ['Lettuce', 'Spinach', 'Kale', 'Arugula', 'Bok Choy',
          'Watercress', 'Mustard Greens', 'Chard', 'Basil', 'Mint']
for plant in plants:
    max_temp = random.uniform(20, 30)
    min_temp = random.uniform(10, 20)
    max_humidity = random.uniform(40, 60)
    min_humidity = random.uniform(20, 40)
    description = fake.sentence()
    cursor.execute("INSERT INTO PlantInfo (name, max_optimal_temperature, min_optimal_temperature, max_optimal_humidity, min_optimal_humidity, description) VALUES (%s, %s, %s, %s, %s, %s);",
                   (plant, max_temp, min_temp, max_humidity, min_humidity, description))

# DB 변경 사항 저장
conn.commit()


# 연결 닫기
cursor.close()
conn.close()
