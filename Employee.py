class Employee():
    def __init__(self: object, emp_id: int, emp_name: str, emp_salary: float):
    self.emp_id = emp_id
    self.emp_name = emp_name
    self.emp_salary = emp_salary

    def new_employee(self, id: int, name: str, sal: float):
        self.emp_id = id
        self.emp_name = name
        self.emp_salary = sal

