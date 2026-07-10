import config
import pandas as pd
from generators.departments import generate_departments

def generate_positions(departments_df):
    department_map = {
        row.DepartmentName: row.DepartmentID
        for _, row in departments_df.iterrows()
    }
    rows = []
    position_id = 1
    for department_name, positions in config.POSITIONS_IN_DEPARTMENTS.items():
        department_id = department_map[department_name]
        for position in positions:
            rows.append({
                "PositionID":position_id,
                "PositionName":position,
                "DepartmentID":department_id
            })
            position_id += 1
    df = pd.DataFrame(rows)
    return df