from sqlalchemy import create_engine, text
import urllib
import config

params = urllib.parse.quote_plus(
    f"DRIVER={{{config.SQL_ODBC_DRIVER}}};"
    f"SERVER={config.SQL_SERVER_NAME};"
    f"DATABASE={config.DATABASE_NAME};"
    f"Trusted_Connection={config.TRUSTED_CONNECTION};"
    f"Encrypt={config.ENCRYPT};"
    f"TrustServerCertificate={config.TRUSTED_SERVER_CERTIFICATE};"
)


def create_database_connection():
    connection_string = f"mssql+pyodbc:///?odbc_connect={params}"
    engine = create_engine(connection_string)

    try:
        connection = engine.connect()
        return connection
    except Exception as e:
        print("Couldn't connect to the database. Error:")
        print(e)


def prepare_load_mode(connection):
    if config.LOAD_MODE == "append":
        pass

    elif config.LOAD_MODE == "replace":
        tables = [
            "Events",
            "Employees",
            "Positions",
            "Devices",
            "Departments"
        ]

        for table in tables:
            query = text(
                f"DELETE FROM dbo.{table}"
            )
            connection.execute(query)

        connection.commit()