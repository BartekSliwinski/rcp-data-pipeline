from sqlalchemy import create_engine, text
import urllib
import config

params = urllib.parse.quote_plus(
    f"DRIVER={{{config.SQL_ODBC_DRIVER}}};"
    f"SERVER={config.SQL_SERVER_NAME};"
    f"DATABASE={config.DATABASE_NAME};"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)


def create_engine_connection():
    connection_string = f"mssql+pyodbc:///?odbc_connect={params}"
    engine = create_engine(connection_string)

    try:
        connection = engine.connect()
        return connection
    except Exception as e:
        print("Couldn't connect to the database. Error:")
        print(e)