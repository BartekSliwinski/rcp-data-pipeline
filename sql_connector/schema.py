

def create_departments_table():
    create_departments = text(
        """
            IF OBJECT_ID('dbo.Departments', 'U') IS NULL
            BEGIN
                CREATE TABLE dbo.Depratments (
                    ID
                )

        """
    )