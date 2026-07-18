from database import create_database_connection, prepare_load_mode
from schema import create_database_schema
from loader import load_all_tables

def main():
    connection = create_database_connection()

    create_database_schema(connection)

    prepare_load_mode(connection)

    load_all_tables(connection)
    
    connection.close()


if __name__ == "__main__":
    main()