-- database 생성
create database aquacycle;

-- admin 계정 생성
create user 'admin'@'%' identified by 'admin';

-- 계정에 권한 부여
grant all privileges on aquacycle.* to 'admin'@'%';
FLUSH PRIVILEGES;

USE AquaCycle;

-- users 테이블 생성
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL, -- 비밀번호는 해시화하여 저장
    email VARCHAR(255) NOT NULL UNIQUE,
    date_joined DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- sensors 테이블 생성
CREATE TABLE sensors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(255) NOT NULL,
    location VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- sensor_data 테이블 생성
CREATE TABLE sensor_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sensor_id INT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    value DOUBLE NOT NULL,
    FOREIGN KEY (sensor_id) REFERENCES sensors(id)
);

-- fish_data 테이블 생성
CREATE TABLE fish_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);

-- plant_data 테이블 생성
CREATE TABLE plant_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);
