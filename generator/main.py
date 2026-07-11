import config
import os
import time
import psutil
from generators.employees import generate_employees
from generators.positions import generate_positions
from generators.departments import generate_departments
from generators.devices import generate_devices
from generators.worklogs import generate_worklogs
from reports.execution_report import generate_report_entry

TOTAL_FILE_SIZE = 0
os.makedirs(config.CSV_OUTPUT_DIRECTORY, exist_ok=True)


def save_dataframe(df, filename, start_time):
    global TOTAL_FILE_SIZE
    path = f"{config.CSV_OUTPUT_DIRECTORY}/{filename}.csv"

    df.to_csv(path, index=False)

    elapsed_time = time.perf_counter() - start_time
    file_size_mb = os.path.getsize(path) / (1024 * 1024)
    TOTAL_FILE_SIZE += file_size_mb
    df_len = len(df)
    print(
        f"✓ {filename}.csv: "
        f"{df_len} records "
        f"({elapsed_time:.3f}s, {file_size_mb:.2f} MB)"
    )
    if filename == "worklogs":
        return df_len


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
    generated_events_count = save_dataframe(worklogs_df, "worklogs", step_start)

    total_time = time.perf_counter() - total_start

    print(f"\nGeneration completed in {total_time:.3f}s")
    process = psutil.Process(os.getpid())
    memory_usage_mb = process.memory_info().rss / 1024 / 1024
    generate_report_entry(total_time,memory_usage_mb, generated_events_count, TOTAL_FILE_SIZE)


if __name__ == "__main__":
    main()