import config
import os
import time
from generate_employees import generate_employees
from generate_positions import generate_positions
from generate_departments import generate_departments
from generate_devices import generate_devices
from generate_worklogs import generate_worklogs


os.makedirs(config.CSV_OUTPUT_DIRECTORY, exist_ok=True)


def save_dataframe(df, filename, start_time):
    path = f"{config.CSV_OUTPUT_DIRECTORY}/{filename}.csv"

    df.to_csv(path, index=False)

    elapsed_time = time.perf_counter() - start_time
    file_size_mb = os.path.getsize(path) / (1024 * 1024)

    print(
        f"✓ {filename}.csv: "
        f"{len(df)} records "
        f"({elapsed_time:.3f}s, {file_size_mb:.2f} MB)"
    )


def main():
    print("Starting data generation...\n")

    total_start = time.perf_counter()

    step_start = time.perf_counter()
    device_df = generate_devices()
    save_dataframe(device_df, "devices", step_start)

    step_start = time.perf_counter()
    departments_df = generate_departments()
    save_dataframe(departments_df, "departments", step_start)

    step_start = time.perf_counter()
    positions_df = generate_positions(departments_df)
    save_dataframe(positions_df, "positions", step_start)

    step_start = time.perf_counter()
    employees_df = generate_employees(positions_df)
    save_dataframe(employees_df, "employees", step_start)

    step_start = time.perf_counter()
    worklogs_df = generate_worklogs(
        employees_df,
        positions_df,
        departments_df
    )
    save_dataframe(worklogs_df, "worklogs", step_start)

    total_time = time.perf_counter() - total_start

    print(f"\nGeneration completed in {total_time:.3f}s")


if __name__ == "__main__":
    main()