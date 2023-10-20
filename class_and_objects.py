"""
Cover class and object defintion
class variables and instance variables
class methods vs instance methods vs static methods
Contructor method - __new__ method creates the object and __init__ method intializes it
Destructor method 
"""

class Employee:

    # class variables
    number_of_leaves = 14

    def __init__(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department
    
    def get_employee_info(self):
        return "Name: {}, Id: {}, Department: {}".format(self.name, self.emp_id, self.department)

    @classmethod
    def update_employee_leaves(cls, leaves_number):
        """
        classmethod can be also used to update class variables but 
        """
        cls.number_of_leaves = leaves_number

    @classmethod
    def from_string(cls, employee_string):
        """
        Eg of how an classmethod can be used as an alternate constructor
        Pydocs datetime module code
        """
        emp_id, name, department = employee_string.split("-")
        return cls(emp_id, name, department)        

    @staticmethod
    def is_holiday(date):
        """
        When no access to class or instance variables and methods is required
        """
        if day.weekday() in [5, 6]:
            return False
        return True

    def __del__(self):
        print("Delting employee {} ....".format(self.name))



emp1 = Employee(1, "John", "IT")
emp2 = Employee(2, "Jane", "Finance")
emp3 = Employee(3, "Mel", "HR")

print(emp1.get_employee_info())
print(emp2.get_employee_info())
print(emp3.get_employee_info())


emp4 = Employee.from_string("4-Kelly-HR")
print(emp4.get_employee_info())


print(emp1.number_of_leaves)
print(emp2.number_of_leaves)

Employee.update_employee_leaves(21)

print(emp1.number_of_leaves)
print(emp2.number_of_leaves)
