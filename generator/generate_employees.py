import config
import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
from generate_positions import generate_positions
from generate_departments import generate_departments

fake = Faker("pl_PL")
random.seed(config.SEED)
Faker.seed(config.SEED)

def get_hire_date():
    start_date = datetime(2020,1,1)
    end_date = datetime.strptime(config.START_DATE, "%Y-%m-%d")
    days_between = (end_date - start_date).days
    random_num_of_days = random.randint(0, days_between)
    random_date = start_date + timedelta(days=random_num_of_days)

    return random_date

def get_status():
    if random.random() < config.ACTIVE_EMPLOYEE_RATIO:
        return "Active"
    else:
        return "Inactive"

def generate_employees(positions_df):
    rows = []
    for employee_id in range(1, config.NUM_OF_EMPLOYEES+1):
        first_name = fake.first_name()
        last_name = fake.last_name()
        position_id = random.choice(positions_df["PositionID"])
        hire_date = get_hire_date()
        status = get_status()
        modified_date = pd.NA
        rows.append({
            "EmployeeID": employee_id,
            "FirstName": first_name,
            "LastName": last_name,
            "PositionID": position_id,
            "HireDate": hire_date,
            "Status": status,
            "ModifiedDate": modified_date
        })
    df = pd.DataFrame(rows)

    return df    

if __name__ == "__main__":
    departments_df = generate_departments()
    positions_df = generate_positions(departments_df)
    df = generate_employees(positions_df)
    print(df)
    df.to_csv("output/employees.csv", index=False)
