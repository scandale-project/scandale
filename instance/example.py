API_HOST = "127.0.0.1"
API_PORT = "8000"
API_URL = "http://127.0.0.1:8000"

DB_USERNAME = "<username>"
DB_PASSWORD = "<password>"
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "scandale"

AUTHENTICATION_REQUIRED = True
USERS = {
    "admin": {
        "password": "Password1234!"
    },
}

CERTIFICATE_FILE = "data/freetsa.crt"
REMOTE_TIMESTAMPER = "http://freetsa.org/tsr"
