import config
import pandas as pd
from datetime import datetime
import holidays

def get_working_days():
    pl_holidays = holidays.country_holidays('PL', years=[2025, 2026])
    custom_pl_business_day = pd.offsets.CustomBusinessDay(holidays=list(pl_holidays.keys()))

    working_days = pd.date_range(start=config.START_DATE, end=config.END_DATE, freq=custom_pl_business_day)
   
    return working_days

def generate_worklogs():
    days = get_working_days()

    for day in days:
        continue

    

if __name__ == "__main__":
    generate_worklogs()
    # days = get_working_days()
    # print(len(days))