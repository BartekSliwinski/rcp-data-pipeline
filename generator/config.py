NUM_OF_EMPLOYEES = 500

YEARS_OF_DATA = 2

START_DATE = "2025-01-01"
END_DATE = "2026-12-31"
WORKING_HOURS_START = 6
WORKING_HOURS_END = 18


SEED = 67

ACTIVE_EMPLOYEE_RATIO = 0.92

IN_OUT_ERROR_RATIO = 0.01
MISSING_CLOCKOUT_RATIO = 0.02
DUPLICATE_LOG_RATIO = 0.01

WORKING_DAYS_PER_WEEK = 5
AVG_SHIFTS_PER_EMPLOYEE = 1

OVERTIME_PROBABILITY = 0.15
SHIFT_DURATION_MEAN = 8
SHIFT_DURATION_STD = 2

POSITIONS_IN_DEPARTMENTS = {
    "IT": [
        "Data Engineer",
        "Data Analyst",
        "Software Developer",
        "DevOps Engineer",
        "QA Engineer",
        "System Administrator"
    ],

    "HR": [
        "HR Specialist",
        "Recruiter",
        "HR Coordinator",
        "HR Business Partner"
    ],

    "Finance": [
        "Accountant",
        "Financial Analyst",
        "Payroll Specialist",
    ],

    "Sales": [
        "Sales Representative",
        "Account Manager",
        "Sales Manager",
        "Business Development Specialist"
    ],

    "Marketing": [
        "Marketing Specialist",
        "Content Manager",
        "Copywriter",
        "SEO Specialist",
        "Graphic Designer"
    ],

    "Production": [
        "Production Operator",
        "Shift Supervisor",
        "Production Planner",
        "Quality Control Specialist"
    ],

    "Warehouse": [
        "Warehouse Worker",
        "Forklift Operator",
        "Logistics Coordinator",
        "Inventory Specialist"
    ],

    "Support": [
        "Customer Support Specialist",
        "Technical Support Engineer",
        "Service Desk Agent",
        "Support Team Lead"
    ]
}
NUM_OF_DEPARTMENTS = len(POSITIONS_IN_DEPARTMENTS)
NUM_OF_POSITIONS = sum(len(dep) for dep in POSITIONS_IN_DEPARTMENTS.values())

DEVICES = [
    "MAIN01", "MAIN02", "MAIN03",
    "SERVICE01", 
    "WAREHOUSE01",
]
NUM_OF_DEVICES = len(DEVICES)