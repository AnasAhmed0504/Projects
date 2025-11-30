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
    def __init__(self, name: str, age: int, salary: int):
        self.name, self.age, self.salary = name, age, salary
    
    def __str__(self):
        return f"Employee {self.name} with age {self.age} has salary {self.salary}"

    def __repr__(self):
        return f"Employee(name={self.name}, age={self.age}, salary={self.salary})"



class EmployeeManager():
    #holds a list of employees and has implementations for the menu functions
    def __init__(self):
        self.__employees = []
    
    def _find(self, name: str):
        name = name.strip()
        for employee in self.__employees:
            if employee.name.lower() == name.lower():
                return employee
        return None
    
    def add_employee(self, name: str, age: int, salary: int):
        name = name.strip()
        if not name:
            print("Name can't be empty.")
            return
        if self._find(name):
            raise ValueError("Employee already exists.")
        if age < 15:
            raise ValueError("Employee must be atleast 15 years")
        
        self.__employees.append(Employee(name, age, salary))
        print(f"Added Empployee: {name}")

    def list_employees(self):
        if len(self.__employees) == 0:
            print("no employees listed.")
            return 
        print('\n**Employees list**')
        return list(self.__employees) # return a copy
    

    def delete_employees_with_age(self, age_from: int, age_to: int):
        before = len(self.__employees)
        self.__employees = [
            emp for emp in self.__employees
            if not (age_from <= emp.age <= age_to)
            ]
        return before - len(self.__employees)
        '''
        It rebuilds the employee list, keeping only employees whose age is NOT in the range.

        In other words:

        “Keep the employees we want to keep.
        Don't keep the employees that match the delete criteria.”
        '''
        
    

    def update_salary_by_name(self, name: str, new_salary: int):
        employee = self._find(name)
        if not employee:
            raise LookupError("Employee not found.")
        old = employee.salary
        employee.salary = new_salary
        print(f"Update salary of {employee.name} from {old} to {new_salary}.")


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
                name = input("Enter name: ").strip()
                age = valid_int_input("enter age: ", 15)
                salary = valid_int_input("Enter salary: ",0)
                self.employees_manager.add_employee(name,age, salary)
            
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

                self.employees_manager.delete_employees_with_age(age_from,age_to)
            
            
            elif choice == 4:
                name = input("Enter Employees name: ").strip()
                salary = valid_int_input("Enter Updated salary: ")

                try:
                    self.employees_manager.update_salary_by_name(name, salary)
                    print("Salary updated.")
                except LookupError as e: 
                    print(e)

            else:
                break

            
if __name__ == '__main__':
    app = FrontendManager()
    app.run()



'''
Some Notes:
*Why LookupError is better than printing errors
-->As using exceptions is senior-level 
-->It separates logic from UI
-->It allows the code to scale
-->It is testable
-->It is reusable
-->It is Pythonic

*LookupError means: “we tried to find (look up) something and it wasn't there”
-->This describes exactly what happened.
-->A senior engineer chooses exception types based on intent, not convenience.


*Why as e is used in:
(except LookupError as e:)
-->This captures the exception object.
e contains:
the message
the exception type
stack trace (if needed)


extra:
print(type(e))    # <class 'LookupError'>
print(str(e))     # Employee not found.


*Python's lookup errors:
-->KeyError → dictionary lookup failure
-->IndexError → list index out of range
-->LookupError → base class for things that “weren't found”

Hierarchy:
Exception
├── LookupError
    ├── IndexError
    └── KeyError

    
** Type hints which are like (age:int)
->>Type hints don't affect runtime, but:
-->help IDEs
-->help future developers
--?reduce bugs
-->improve readability
-->A senior uses type hints because they make the contract of the function clear.


**Your original code used:
(for idx in range(len(self.employees)-1,-1,-1):)

>>>a better approach
The list comprehension (the core logic)
self._employees = [
    emp for emp in self._employees
    if not (age_from <= emp.age <= age_to)
]
>>>why is it better
-->No manual index manipulation
-->No mutation during iteration
/Removing items while iterating is dangerous.
/List comprehension avoids this problem.

-->Clear intent
/The senior code expresses intention:
/“Rebuild the list, keeping only employees we want.”
/This is called declarative programming.

-->Faster
List comprehensions are optimized in CPython.

-->Readability
Every senior Python engineer instantly recognizes this pattern.


*Seniors try to avoid any printing in service logic.
-->UI prints → OK
-->Backend prints → try to avoid
'''