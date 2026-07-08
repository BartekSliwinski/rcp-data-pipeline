import config
import pandas as pd
from datetime import datetime, timedelta
import holidays
import random
from generate_employees import generate_employees
from generate_positions import generate_positions
from generate_departments import generate_departments
from generate_devices import generate_devices

random.seed(config.SEED)

def get_working_days():
    pl_holidays = holidays.country_holidays('PL', years=[2025, 2026])
    custom_pl_business_day = pd.offsets.CustomBusinessDay(holidays=list(pl_holidays.keys()))

    working_days = pd.date_range(start=config.SIMULATION_START_DATE, end=config.SIMULATION_END_DATE, freq=custom_pl_business_day)
   
    return working_days

def create_employee_devices_lookup(employees_df, positions_df, departments_df):
    wynik = positions_df.merge(employees_df, on="PositionID", how="left")
    wynik1 = departments_df.merge(wynik, on="DepartmentID", how="left")
    wynik1.sort_values(["EmployeeID"], inplace=True)

    employee_in_department = dict(zip(wynik1["EmployeeID"], wynik1["DepartmentName"]))
    employee_devices = {}
    for employee_id, dept_name in employee_in_department.items():
        employee_devices[employee_id] = config.DEPARTMENT_DEVICES.get(dept_name, ["MAIN01", "MAIN02", "MAIN03"])
    return employee_devices


def get_start_offset():
    seconds = random.randint(0, 14400)
    return seconds

def get_shift_duration():
    shift_duration = random.gauss(config.SHIFT_DURATION_MEAN, config.SHIFT_DURATION_STD)
    return shift_duration

def missing_event():
    if random.random() < config.MISSING_EVENT_RATIO:
        return True
    else: 
        return False

def missing_start_or_end_of_shift():
    if random.random() < 0.5:
        return "start"
    else: 
        return "end"

def duplicate_event():
    if random.random() < config.DUPLICATE_LOG_RATIO:
        return True
    else:
        return False
    
def duplicated_start_or_end_of_shift():
    if random.random() < 0.5:
        return "start"
    else: 
        return "end"

def generate_worklogs(employees_df, positions_df, departments_df):
    employee_devices_lookup = create_employee_devices_lookup(employees_df, positions_df, departments_df)
    
    days = get_working_days()
    work_log_id = 1
    rows = []
    for day in days:
        employees_that_worked_that_day = employees_df[(employees_df["HireDate"] <= day) & ((employees_df["Status"] == "Active") | (employees_df["ModifiedDate"] > day))]
        active_ids = employees_that_worked_that_day["EmployeeID"].to_list()

        for employee_id in active_ids:
            one_of_events_is_missing = missing_event()
            if one_of_events_is_missing:
                missing_event_is = missing_start_or_end_of_shift()
            else: 
                missing_event_is = 0
            event_is_duplicated = duplicate_event()
            if event_is_duplicated:
                duplicated_event = duplicated_start_or_end_of_shift()
            else: 
                duplicated_event = 0
            starting_time = day + timedelta(hours=config.WORKING_HOURS_START)+ timedelta(seconds=get_start_offset())
            device = random.choice(list(employee_devices_lookup[employee_id]))
            if missing_event_is != "start":
                rows.append({
                    "WorkLogID": work_log_id,
                    "EmployeeID": employee_id,
                    "DeviceID": device,
                    "EventType": "IN",
                    "EventTime": starting_time
                })
                work_log_id += 1
                if duplicated_event == "start":
                    rows.append({
                    "WorkLogID": work_log_id,
                    "EmployeeID": employee_id,
                    "DeviceID": device,
                    "EventType": "IN",
                    "EventTime": starting_time + timedelta(seconds=2)
                })
                work_log_id += 1
            if missing_event_is != "end":
                rows.append({
                    "WorkLogID": work_log_id,
                    "EmployeeID": employee_id,
                    "DeviceID": device,
                    "EventType": "OUT",
                    "EventTime": starting_time + timedelta(hours=round(get_shift_duration(), 2))
                })
                work_log_id += 1
                if duplicated_event == "end":
                    rows.append({
                    "WorkLogID": work_log_id,
                    "EmployeeID": employee_id,
                    "DeviceID": device,
                    "EventType": "OUT",
                    "EventTime": starting_time + timedelta(hours=round(get_shift_duration(), 2)) + timedelta(seconds=2)
                })
                work_log_id += 1



    df = pd.DataFrame(rows)
    df = df.sort_values(by=["EventTime"], ascending=True)
    return df
    

def main():
    departments_df = generate_departments()
    positions_df = generate_positions(departments_df)
    employees_df = generate_employees(positions_df)

    df = generate_worklogs(employees_df, positions_df, departments_df)
    print(df)
    df.to_csv(f"{config.CSV_OUTPUT_DIRECTORY}/worklogs.csv", index=False)

if __name__ == "__main__":
    main()
