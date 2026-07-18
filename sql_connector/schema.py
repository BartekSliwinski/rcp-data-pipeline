from sqlalchemy import text

def create_departments_table(connection):
    create_departments_query = text(
        """
        IF OBJECT_ID('dbo.Departments', 'U') IS NULL
        BEGIN
            CREATE TABLE dbo.Departments (
                DepartmentID INT IDENTITY(1,1) PRIMARY KEY,
                DepartmentName VARCHAR(30) NOT NULL UNIQUE
            );
        END
        """
    )
    connection.execute(create_departments_query)
    connection.commit()


def create_positions_table(connection):
    create_positions_query = text(
        """
        IF OBJECT_ID('dbo.Positions', 'U') IS NULL
        BEGIN
            CREATE TABLE dbo.Positions (
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
    connection.commit()


def create_employees_table(connection):
    create_employees_query = text(
        """
        IF OBJECT_ID('dbo.Employees', 'U') IS NULL
        BEGIN
            CREATE TABLE dbo.Employees (
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
    connection.commit()


def create_devices_table(connection):
    create_devices_query = text(
        """
        IF OBJECT_ID('dbo.Devices', 'U') IS NULL
        BEGIN
            CREATE TABLE dbo.Devices (
                DeviceID INT IDENTITY(1,1) PRIMARY KEY,
                DeviceName VARCHAR(20) NOT NULL UNIQUE
            );
        END
        """
    )
    connection.execute(create_devices_query)
    connection.commit()


def create_events_table(connection):
    create_events_query = text(
        """
        IF OBJECT_ID('dbo.Events', 'U') IS NULL
        BEGIN
            CREATE TABLE dbo.Events (
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
    connection.commit()


def create_database_schema(connection):
    create_departments_table(connection)
    create_positions_table(connection)
    create_employees_table(connection)
    create_devices_table(connection)
    create_events_table(connection)