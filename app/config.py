# Security
SECRET_KEY = 'S4Eye4bf'
BLACKLIST = set()

# Database
DB_DRIVE = "sqlite"
DB_PATH = "/tmp/test.db"  # Just for sqlite
DB_HOST = "database"
DB_DATABASE = "flask"
DB_PORT = 3306
DB_USER = "root"
DB_PASSWORD = "flask"

if DB_DRIVE == "sqlite":
    DATABASE_URI = f"{DB_DRIVE}:///{DB_PATH}"
else:
    DATABASE_URI = f"{DB_DRIVE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

# Application
HOST_ALLOW = "0.0.0.0"
PORT = 5000
DEBUG = True