from sqlalchemy import text

from logger import get_logger

logger = get_logger(__name__)


def create_departments_table(connection):
    table_name = "Departments"
    try:
        create_departments_query = text(
            f"""
            IF OBJECT_ID('dbo.{table_name}', 'U') IS NULL
            BEGIN
                CREATE TABLE dbo.{table_name} (
                    DepartmentID INT IDENTITY(1,1) PRIMARY KEY,
                    DepartmentName VARCHAR(30) NOT NULL UNIQUE
                );
            END
            """
        )
        connection.execute(create_departments_query)
        logger.info(f"Table ready: {table_name}")

    except Exception:
        logger.exception(f"Failed creating table: {table_name}")
        raise


def create_positions_table(connection):
    table_name = "Positions"
    try:
        create_positions_query = text(
            f"""
            IF OBJECT_ID('dbo.{table_name}', 'U') IS NULL
            BEGIN
                CREATE TABLE dbo.{table_name} (
                    PositionID INT IDENTITY(1,1) PRIMARY KEY,
                    PositionName VARCHAR(60) NOT NULL UNIQUE,
                    DepartmentID INT NOT NULL,

                    CONSTRAINT FK_Positions_Departments
                    FOREIGN KEY (DepartmentID) REFERENCES dbo.Departments(DepartmentID)
                );
            END
            """
        )
        connection.execute(create_positions_query)
        logger.info(f"Table ready: {table_name}")
        
    except Exception:
        logger.exception(f"Failed creating table: {table_name}")
        raise


def create_employees_table(connection):
    table_name = "Employees"
    try:
        create_employees_query = text(
            f"""
            IF OBJECT_ID('dbo.{table_name}', 'U') IS NULL
            BEGIN
                CREATE TABLE dbo.{table_name} (
                    EmployeeID INT IDENTITY(1,1) PRIMARY KEY,
                    FirstName VARCHAR(20) NOT NULL,
                    LastName VARCHAR(20) NOT NULL,
                    PositionID INT NOT NULL,
                    PhoneNumber VARCHAR(9) NOT NULL UNIQUE,
                    Email VARCHAR(60) NOT NULL UNIQUE,
                    Status VARCHAR(10) NOT NULL,
                    HireDate DATETIME2 NOT NULL,
                    ModifiedDate DATETIME2 NOT NULL,

                    CONSTRAINT FK_Employees_Positions
                        FOREIGN KEY (PositionID)
                        REFERENCES dbo.Positions(PositionID),

                    CONSTRAINT CK_Employees_Status
                        CHECK (Status IN ('Active','Inactive'))
                );
            END
            """
        )
        connection.execute(create_employees_query)
        logger.info(f"Table ready: {table_name}")
        
    except Exception:
        logger.exception(f"Failed creating table: {table_name}")
        raise


def create_devices_table(connection):
    table_name = "Devices"
    try:
        create_devices_query = text(
            f"""
            IF OBJECT_ID('dbo.{table_name}', 'U') IS NULL
            BEGIN
                CREATE TABLE dbo.{table_name} (
                    DeviceID INT IDENTITY(1,1) PRIMARY KEY,
                    DeviceName VARCHAR(20) NOT NULL UNIQUE
                );
            END
            """
        )
        connection.execute(create_devices_query)
        logger.info(f"Table ready: {table_name}")
        
    except Exception:
        logger.exception(f"Failed creating table: {table_name}")
        raise


def create_events_table(connection):
    table_name = "Events"
    try:
        create_events_query = text(
            f"""
            IF OBJECT_ID('dbo.{table_name}', 'U') IS NULL
            BEGIN
                CREATE TABLE dbo.{table_name} (
                    EventID INT IDENTITY(1,1) PRIMARY KEY,
                    EmployeeID INT NOT NULL,
                    DeviceID INT NOT NULL,
                    EventType VARCHAR(10) NOT NULL,
                    EventTime DATETIME2 NOT NULL,

                    CONSTRAINT FK_Events_Employees
                        FOREIGN KEY (EmployeeID)
                        REFERENCES dbo.Employees(EmployeeID),

                    CONSTRAINT FK_Events_Devices
                        FOREIGN KEY (DeviceID)
                        REFERENCES dbo.Devices(DeviceID),

                    CONSTRAINT CK_Events_Type
                        CHECK (EventType IN ('IN','OUT'))
                );
            END
            """
        )
        connection.execute(create_events_query)
        logger.info(f"Table ready: {table_name}")
        
    except Exception:
        logger.exception(f"Failed creating table: {table_name}")
        raise


def create_database_schema(connection):
    try:
        logger.info("Creating database schema.")
        create_departments_table(connection)
        create_positions_table(connection)
        create_employees_table(connection)
        create_devices_table(connection)
        create_events_table(connection)
        connection.commit()
        logger.info("Database schema created successfully.")

    except Exception:
        connection.rollback()
        logger.exception("Failed creating database schema.")
        raise