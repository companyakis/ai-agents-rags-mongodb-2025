def create_employee_data(name: str, id: str, department: str, title: str, salary: int) :

    return (name, id, department, title, salary)

emp1 = create_employee_data("Ayhan", "101", "HR", "Senior Expert", 75500)

print(emp1) # ('Ayhan', '101', 'HR', 'Senior Expert', 75500)
