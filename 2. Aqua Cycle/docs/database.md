1. **테이블 설계**

   1.1. `users`

   - `id`: 유저 ID (Primary Key, Auto Increment)
   - `username`: 유저 이름 (Unique)
   - `password`: 비밀번호 (해쉬 처리)
   - `email`: 이메일
   - `date_joined`: 가입 날짜

     1.2. `sensors`

   - `id`: 센서 ID (Primary Key, Auto Increment)
   - `user_id`: 센서를 등록한 유저의 ID (Foreign Key to `users.id`)
   - `name`: 센서 이름
   - `type`: 센서 유형 (예: 온도, 습도 등)
   - `location`: 센서 위치

     1.3. `sensor_data`

   - `id`: 데이터 ID (Primary Key, Auto Increment)
   - `sensor_id`: 데이터가 속한 센서의 ID (Foreign Key to `sensors.id`)
   - `timestamp`: 데이터 측정 시각
   - `value`: 측정된 값

     1.4. `fish_data`

   - `id`: 데이터 ID (Primary Key, Auto Increment)
   - `name`: 물고기 이름
   - `description`: 물고기에 대한 설명

     1.5. `plant_data`

   - `id`: 데이터 ID (Primary Key, Auto Increment)
   - `name`: 식물 이름
   - `description`: 식물에 대한 설명

2. **테이블 관계**

   2.1. `users`와 `sensors`

   - 1:N 관계
   - 한 명의 유저는 여러 센서를 가질 수 있음

     2.2. `sensors`와 `sensor_data`

   - 1:N 관계
   - 한 개의 센서는 여러 데이터를 가질 수 있음

3. **관계 정리**

   - 한 명의 유저는 여러 센서를 등록할 수 있다. (`users` → `sensors`)
   - 한 개의 센서는 여러 데이터를 측정하여 저장할 수 있다. (`sensors` → `sensor_data`)
   - 물고기 데이터(`fish_data`)와 식물 데이터(`plant_data`)는 단순한 정보를 위한 테이블로서 특정한 외부 키 관계는 갖지 않는다.

데이터베이스 구조를 기반으로 SQL 쿼리를 작성하여 테이블 생성하고, Flask 애플리케이션에서 이를 사용하여 CRUD 연산 수행.
