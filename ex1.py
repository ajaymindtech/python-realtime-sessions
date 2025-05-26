employees = [
    {"name": "Ajay", "salary": 120000},
    {"name": "Vijay", "salary": 95000},
    {"name": "Sita", "salary": 150000},
    {"name": "Rita", "salary": 80000},
]

for emp in employees:
    if emp["salary"] > 100000:
        print(f"{emp['name']} has a salary of {emp['salary']}")
        
        
        
employees = [
    {"name": "Ajay", "salary": 120000},
    {"name": "Vijay", "salary": 95000},
    {"name": "Sita", "salary": 150000},
    {"name": "Rita", "salary": 80000},
]

high_salary_emps = [emp for emp in employees if emp["salary"] > 100000]

for emp in high_salary_emps:
    print(f"{emp['name']} has a salary of {emp['salary']}")