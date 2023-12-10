import os
import urllib.parse
from sqlalchemy import create_engine, exc, text


def check_db_health():
    username = os.getenv("DB_USERNAME")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db = os.getenv("DB_NAME")
    printable_conn_str = f'postgresql://{username}:xxxx@{host}:{port}/{db}'
    
    print(f"Connecting to: {printable_conn_str}")
    try:
        engine = create_engine(generate_connection_string())
        con = engine.connect()
        con.execute(text("SELECT 1"))
        return True
    except exc.SQLAlchemyError as ex:
        return False


def generate_connection_string():
    # Read database credentials directly from environment variables
    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")

    if not username or password is None:
        raise EnvironmentError("Database credentials (username or password) not set in environment variables.")

    encoded_password = urllib.parse.quote_plus(password)

    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db = os.getenv("DB_NAME")

    if not host or not port or not db:
        raise EnvironmentError("Database connection details (host, port, or dbname) not set in environment variables.")

    # SSL parameters
    sslmode = os.getenv("DB_SSL_MODE")
    sslrootcert = os.getenv("DB_SSL_SERVER_CA")
    sslcert = os.getenv("DB_SSL_CLIENT_CA")
    sslkey = os.getenv("DB_SSL_CLIENT_KEY")

    # Constructing the connection string
    connection_string = f'postgresql://{username}:{encoded_password}@{host}:{port}/{db}'

    # Adding SSL parameters if they exist
    ssl_params = []
    if sslmode:
        ssl_params.append(f"sslmode={sslmode}")
    if sslrootcert:
        ssl_params.append(f"sslrootcert={urllib.parse.quote_plus(sslrootcert)}")
    if sslcert:
        ssl_params.append(f"sslcert={urllib.parse.quote_plus(sslcert)}")
    if sslkey:
        ssl_params.append(f"sslkey={urllib.parse.quote_plus(sslkey)}")

    if ssl_params:
        connection_string += "?" + "&".join(ssl_params)

    return connection_string

