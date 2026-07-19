from database import create_database_connection, prepare_load_mode
from schema import create_database_schema
from loader import load_all_tables
from logger import get_logger

logger = get_logger(__name__)


def main():
    connection = None

    try:
        logger.info("Starting SQL Connector process.")
        connection = create_database_connection()
        create_database_schema(connection)
        prepare_load_mode(connection)
        load_all_tables(connection)
        logger.info("SQL Connector process completed successfully.")
    
    except Exception:
        logger.exception("SQL Connector process failed.")
        raise

    finally:
        if connection is not None:
            connection.close()
            logger.info("Database connection closed.")


if __name__ == "__main__":
    main()