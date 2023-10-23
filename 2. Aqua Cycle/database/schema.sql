-- Users Table: 사용자 정보
CREATE TABLE Users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX(email)
);

-- Systems Table: 아쿠아포닉스 시스템 정보
CREATE TABLE Systems (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    name VARCHAR(80),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    INDEX(user_id)
);

-- SensorTypes Table
CREATE TABLE SensorTypes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    type_name VARCHAR(50)
);

-- Sensor Table: 센서
CREATE TABLE Sensors (
    id INT PRIMARY KEY AUTO_INCREMENT,
    system_id INT,
    sensor_type_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (system_id) REFERENCES Systems(id),
    FOREIGN KEY (sensor_type_id) REFERENCES SensorTypes(id),
    INDEX(system_id),
    INDEX(sensor_type_id)
);

-- SensorData Table: 센서 데이터
CREATE TABLE SensorData (
    id INT PRIMARY KEY AUTO_INCREMENT,
    sensor_id INT,
    value FLOAT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sensor_id) REFERENCES Sensors(id),
    INDEX(sensor_id)
);

-- FishInfo table: 물고기 정보
CREATE TABLE FishInfo (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    max_optimal_temperature FLOAT,
    min_optimal_temperature FLOAT,
    max_optimal_water_quality FLOAT,
    min_optimal_water_quality FLOAT,
    description VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- PlantInfo table: 식물 정보
CREATE TABLE PlantInfo (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    max_optimal_temperature FLOAT,
    min_optimal_temperature FLOAT,
    max_optimal_humidity FLOAT,
    min_optimal_humidity FLOAT,
    description VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- SystemFish table: 아쿠아포닉스 시스템과 물고기 정보의 매핑
CREATE TABLE SystemFish (
    system_id INT,
    fish_id INT,
    FOREIGN KEY (system_id) REFERENCES Systems(id),
    FOREIGN KEY (fish_id) REFERENCES FishInfo(id),
    PRIMARY KEY (system_id, fish_id)
);

-- SystemPlant table: 아쿠아포닉스 시스템과 식물 정보의 매핑
CREATE TABLE SystemPlant (
    system_id INT,
    plant_id INT,
    FOREIGN KEY (system_id) REFERENCES Systems(id),
    FOREIGN KEY (plant_id) REFERENCES PlantInfo(id),
    PRIMARY KEY (system_id, plant_id)
);
