from sqlalchemy import text
import pandas as pd

import config
from logger import get_logger

logger = get_logger(__name__)


def switch_identity_insert(table_name, connection, switch):
    query = text(
        f"""
        SET IDENTITY_INSERT dbo.{table_name} {switch};
        """
    )

    connection.execute(query)
    connection.commit()


def load_csv_to_table(connection, db_table_name, csv_file_name):
    identity_enabled = False

    try:
        logger.info(f"Loading file: {csv_file_name} into table: {db_table_name}")

        switch_identity_insert(
            db_table_name,
            connection,
            "ON"
        )
        identity_enabled = True

        csv_file_path = config.CSV_DIRECTORY / csv_file_name

        df = pd.read_csv(
            csv_file_path,
            encoding="utf-8"
        )

        df.to_sql(
            name=db_table_name,
            con=connection,
            schema="dbo",
            if_exists="append",
            index=False
        )

        logger.info(
            f"Successfully loaded {len(df)} records into table: {db_table_name}"
        )

    except Exception:
        logger.exception(
            f"Failed loading file: {csv_file_name} into table: {db_table_name}"
        )
        raise

    finally:
        if identity_enabled:
            try:
                switch_identity_insert(
                    db_table_name,
                    connection,
                    "OFF"
                )
            except Exception:
                logger.exception(
                    f"Failed disabling IDENTITY_INSERT for table: {db_table_name}"
                )
                raise


def load_all_tables(connection):
    tables = [
        ("Departments", "departments.csv"),
        ("Positions", "positions.csv"),
        ("Employees", "employees.csv"),
        ("Devices", "devices.csv"),
        ("Events", "events.csv")
    ]

    logger.info("Starting data loading process.")

    for table, csv_file in tables:
        load_csv_to_table(
            connection,
            table,
            csv_file
        )

    logger.info("Data loading process completed successfully.")