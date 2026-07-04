import config
import pandas as pd

def generate_departments():
    df = pd.DataFrame({
        "DepartmentID": range(1, config.NUM_OF_DEPARTMENTS+1),
        "DepartmentName": list(config.POSITIONS_IN_DEPARTMENTS.keys())
    })

    return df

if __name__ == "__main__":
    df = generate_departments()
    print(df)
    df.to_csv("output/departments.csv", index=False)