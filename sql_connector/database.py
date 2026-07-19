from sqlalchemy import create_engine, text
import urllib

import config
from logger import get_logger

logger = get_logger(__name__)

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
        logger.info(f"Successfully established connection to database: {config.DATABASE_NAME}")
        return connection
    except Exception:
        logger.exception(
            f"Could not connect to database: {config.DATABASE_NAME}"
        )
        raise


def prepare_load_mode(connection):
    if config.LOAD_MODE == "append":
        pass

    elif config.LOAD_MODE == "replace":
        logger.warning("Database load mode: REPLACE. All existing data will be deleted before importing new data.")
        
        try:
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
            logger.info(
                "Existing database data cleared successfully."
            )

        except Exception:
            logger.exception(
                "Failed to clear existing database data before loading new data."
            )
            raise

    else:
        raise ValueError(
            f"Unsupported database load mode: {config.LOAD_MODE}"
        )