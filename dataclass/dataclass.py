from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    age: int
    department: str
    salary: float

def add_employee(employees, employee):
    employees.append(employee)
    print(f"{employee.name} has been added to the system.")

def display_employees(employees):
    print("\nEmployee Details:")
    for employee in employees:
        print(f"Name: {employee.name}, Age: {employee.age}, Department: {employee.department}, Salary: {employee.salary}")

def update_employee_salary(employees, name, new_salary):
    for employee in employees:
        if employee.name == name:
            employee.salary = new_salary
            print(f"Salary updated for {name} to {new_salary}.")
            return
    print(f"Employee with name {name} not found.")

def remove_employee(employees, name):
    for employee in employees:
        if employee.name == name:
            employees.remove(employee)
            print(f"{name} has been removed from the system.")
            return
    print(f"Employee with name {name} not found.")

# Sample usage
if __name__ == "__main__":
    # Create an empty list to store employee objects
    employee_list = []

    # Add employees to the system
    add_employee(employee_list, Employee("Juan Martin", 21, "IT", 250000.0))
    add_employee(employee_list, Employee("Silvia", 27, "HR", 45000.0))

    # Display details of all employees
    display_employees(employee_list)

    # Update employee salary
    update_employee_salary(employee_list, "Silvia", 55000.0)

    # Remove an employee
    remove_employee(employee_list, "Juan Martin")

    # Display updated details of remaining employees
    display_employees(employee_list)
