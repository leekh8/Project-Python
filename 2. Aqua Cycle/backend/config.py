import os

# Database configurations — override via environment variables.
# Defaults are local-development placeholders only (do not use in production).
DATABASE_USERNAME = os.environ.get('DATABASE_USERNAME', 'admin')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'admin')
DATABASE_HOSTNAME = os.environ.get('DATABASE_HOSTNAME', 'localhost')
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'aquacycle')
DATABASE_URI = f'mysql+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOSTNAME}/{DATABASE_NAME}'
