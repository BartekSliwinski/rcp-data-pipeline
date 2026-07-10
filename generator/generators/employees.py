import config
import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
from generators.positions import generate_positions
from generators.departments import generate_departments
from unidecode import unidecode

fake = Faker("pl_PL")
random.seed(config.SEED)
Faker.seed(config.SEED)

def get_hire_date():
    start_date = datetime.strptime(config.HIRING_STARTING_DATE, "%Y-%m-%d")
    end_date = datetime.strptime(config.SIMULATION_START_DATE, "%Y-%m-%d")

    days_between = (end_date - start_date).days
    random_num_of_days = random.randint(0, days_between)
    random_date = start_date + timedelta(days=random_num_of_days)

    return random_date

def get_status():
    if random.random() < config.ACTIVE_EMPLOYEE_RATIO:
        return "Active"
    else:
        return "Inactive"
    
def get_modified_date(hire_date):
    end_date = datetime.strptime(config.SIMULATION_END_DATE, "%Y-%m-%d")

    days_between = (end_date - hire_date).days
    random_num_of_days = random.randint(0, days_between)
    random_date = hire_date + timedelta(days=random_num_of_days)

    return random_date

def get_phone_number():
    prefixes = [
        "501", "502", "503",
        "511", "512",
        "601", "602",
        "691", "692",
        "721", "731", "797",
        "881"
    ]
    phone_number = random.choice(prefixes) + fake.numerify("######")
    return phone_number

def get_email(first_name, last_name):
    email_formats = [
        "firstlast",
        "lastfirst",
        "flast",
        "first.last",
        "last.first",
        "last_and_numbers",
        "first_3_letters_of_both"
    ]

    domains = [
        "gmail.com",
        "wp.pl",
        "onet.pl",
        "interia.pl",
        "vp.pl",
        "proton.com",
        "outlook.com"
    ]
    first_name = unidecode(first_name)
    last_name = unidecode(last_name)
    email = ""
    chosen_format = random.choice(email_formats)
    match chosen_format:
        case "firstlast":
            email += first_name + last_name
        case "lastfirst":
            email += last_name + first_name
        case "flast":
            email += first_name[0] + last_name
        case "first.last":
            email += first_name + "." + last_name
        case "last.first":
            email += last_name + "." + first_name
        case "last_and_numbers":
            email += last_name + fake.numerify("###")
        case "first_3_letters_of_both":
            email += first_name[:3] + last_name[:3]
    email_domain = random.choice(domains)
    return email+ "@" + email_domain

def generate_employees(positions_df):
    rows = []
    for employee_id in range(1, config.NUM_OF_EMPLOYEES+1):
        first_name = fake.first_name()
        last_name = fake.last_name()
        position_id = random.choice(positions_df["PositionID"])
        phone_number = get_phone_number()
        email = get_email(first_name, last_name)
        hire_date = get_hire_date()
        status = get_status()
        modified_date = get_modified_date(hire_date)
        rows.append({
            "EmployeeID": employee_id,
            "FirstName": first_name,
            "LastName": last_name,
            "PositionID": position_id,
            "PhoneNumber": phone_number,
            "Email": email,
            "HireDate": hire_date,
            "Status": status,
            "ModifiedDate": modified_date
        })
    df = pd.DataFrame(rows)
    return df    
