from sqlalchemy import text
import pandas as pd
import config

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
        switch_identity_insert(db_table_name, connection, "ON")
        identity_enabled = True
        csv_file_path = config.CSV_DIRECTORY / csv_file_name
        df = pd.read_csv(csv_file_path, encoding='utf-8')

        df.to_sql(
            name=db_table_name,
            con=connection,
            schema='dbo',
            if_exists="append",
            index=False
        )

    except Exception as e:
        print("Wystąpił błąd podczas ładowania danych:")
        print(e)
    finally:
        if identity_enabled:
            switch_identity_insert(db_table_name, connection, "OFF")

def load_all_tables(connection):
    tables = [
        ("Departments", "departments.csv"),
        ("Positions", "positions.csv"),
        ("Employees", "employees.csv"),
        ("Devices", "devices.csv"),
        ("Events", "events.csv")
    ]
    for table, csv_file in tables:
        load_csv_to_table(connection, table, csv_file)