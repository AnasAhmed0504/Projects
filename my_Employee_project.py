"""
1)add new employee
2)print all employees
3)delete by age
4)update salary by name
5)end the program

"""

def valid_int_input(msg, start = 0, end = None):
    while True:
        try:
            inp = int(input(msg))
            if start is not None and end is not None and (inp < start or inp > end):
                print(f"input must be >= {start} and <= {end}")
                continue
            return inp

            
        except ValueError:
            print("Invalide input, plz Enter a valid input: ")
    


class Employee():
    #just holds the data and basic functions
    def __init__(self, name, age, salary):
        self.name, self.age, self.salary = name, age, salary
    
    def __str__(self):
        return f"Employee {self.name} with age {self.age} has salary {self.salary}"

    def __repr__(self):
        return f"Employee(name={self.name}, age={self.age}, salary={self.salary})"

class EmployeeManager():
    #holds a list of employees and has implementations for the menu functions
    def __init__(self):
        self.employees = []
    
    def add_emloyees(self, name, age, salary):
        for emp in self.employees:
            if emp.name == name:
                print("Employee with such name is already Found.")
                return

        self.employees.append(Employee(name, age, salary))
        print(f"Added Empployee: {name}")

    def list_employees(self):
        if len(self.employees) == 0:
            print("no employees listed.")
            return 
        print('\n**Employees list**')
        for emp in self.employees:
            print(emp)
    

    def delete_empoloyees_with_age(self, age_from, age_to):
        for idx in range(len(self.employees)-1,-1,-1):
            emp = self.employees[idx]
            if age_from <= emp.age <= age_to:
                print(f"\tDeleting employee {emp.name}")
                self.employees.pop(idx)
            else: 
                print("No Employees with age in this range is found.")

    def find_employee_by_name(self, name):
        for employee in self.employees:
            if employee.name == name:
                return employee
        return None

    def update_salary_by_name(self, name, salary):
        employee = self.find_employee_by_name(name)
        if employee == None:
            print("Not Found.")
        else:
            employee.salary = salary


class FrontendManager():
    #print the menu, get a choice and call the EmployeeManager
    def __init__(self):
        self.employees_manager = EmployeeManager()
    
    def menu(self):
        menu = ["1)add new employee",
                "2)print all employees",
                "3)delete by age",
                "4)update salary by name",
                "5)end the program"]
       
        print("\n".join(menu))
        msg = f"Enter your choice from 1 to {len(menu)}: "
        return valid_int_input(msg, 1, len(menu))

    def run(self):
       

        while(True):
            choice = self.menu()

            if choice == 1:
                print("Enter Employees Data: ")
                name = input("Enter name: ")
                age = int(input("enter age: "))
                salary = int(input("Enter salary: "))
                self.employees_manager.add_emloyees(name,age, salary)
            
            elif choice == 2:
                self.employees_manager.list_employees()
            
            elif choice == 3:
                while True:
                    try:
                        age_from = valid_int_input("Enter age from: ")
                        age_to = valid_int_input("Enter age to: ")

                        if age_from < age_to:
                            break
                        else:
                            print("Error: 'age from' must be LESS than 'age to'. Try again.\n")

                    except ValueError:
                        print("Error: please enter valid integers.\n")

                self.employees_manager.delete_empoloyees_with_age(age_from,age_to)
            
            
            elif choice == 4:
                name = input("Enter Employees name: ")
                salary = valid_int_input("Enter Updated salary: ")
                self.employees_manager.update_salary_by_name(name, salary)
            
            else:
                break

            
if __name__ == '__main__':
    app = FrontendManager()
    app.run()
