# 디렉토리 구조

```
AquaCycle/
│
├── backend/ # 백엔드 코드
│ ├── app.py # Flask 어플리케이션
│ ├── models.py # 데이터베이스 모델
│ ├── routes.py # API 라우터
│ └── config.py # 설정 파일
│
├── frontend/ # 프론트엔드 코드
│ ├── public/
│ │ └── index.html
│ ├── src/
│ │ ├── App.js # 메인 React 컴포넌트
│ │ ├── Components/ # 부가 컴포넌트들
│ │ └── ...
│ └── package.json
│
├── database/ # 데이터베이스 설정과 스키마
│ └── schema.sql
│
└── README.md # 프로젝트 설명
```

# Index

## Backend (Python + Flask)

- app.py: Flask 웹 서버 설정 및 초기화
- models.py: MySQL 데이터베이스의 테이블 구조 및 모델 정의
- routes.py: API 엔드포인트 및 라우팅 설정
- config.py: 설정 값 저장 (DB 접속 정보, Secret Key 등)

## Frontend (React)

- App.js: 메인 애플리케이션 컴포넌트. API 호출 및 상태 관리
- Components/: 아쿠아포닉스 시스템의 센서 값을 표시할 컴포넌트, 사용자 인터페이스 등

## Database (MySQL)

- schema.sql: 초기 데이터베이스 스키마 설정 파일

  - Users: 사용자 정보
  - Systems: 아쿠아포닉스 시스템 정보
  - Sensors: 센서 데이터 (수온, 온도, 습도, 수위, 수질)

## APIs

- 사용자 등록 및 인증
- 아쿠아포닉스 시스템 정보 조회 및 수정
- 센서 데이터 입력, 조회, 수정

## User Experience

- 사용자는 웹 인터페이스를 통해 아쿠아포닉스 시스템의 상태를 실시간으로 확인 가능
- 시스템 및 센서는 사용자 별로 나뉘어 관리

## Data Flow

- 센서 -> Backend -> Database -> Frontend
