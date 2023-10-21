"""
Types of inheritance
  - Single
  - Multiple
  - Multilevel
  - Hierachial
  
super()
to call parent class methods in child 

issubclass(class, )
check is class is child of a parent

isinstance()
check if object is instance of a particular class

Method overriding
Override parent class method - DRF APIView - override get req method

Method Order resolution MRO
C.mro()
[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
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
        pass
        # print("Delting employee {} ....".format(self.name))


class Developer(Employee):
    number_of_leaves = 21

    def __init__(self, emp_id, name, department, coding_lang):
        super().__init__(emp_id, name, department)
        self.coding_lang = coding_lang


class Manager(Employee):
    number_of_leaves = 29

    def __init__(self, emp_id, name, department, employees=None):
        super().__init__(emp_id, name, department)

        if employees:
            self.employees = employees
        else:
            self.employees = []

    def print_all_employees(self):
        print("ALL EMPLOYEES")
        for emp in self.employees:
            print(emp.get_employee_info())
        


emp1 = Employee(1, "John", "IT")
emp2 = Employee(2, "Jane", "Finance")
emp3 = Employee(3, "Mel", "HR")

# print(emp1.get_employee_info())
# print(emp2.get_employee_info())
# print(emp3.get_employee_info())


emp4 = Employee.from_string("4-Kelly-HR")
# print(emp4.get_employee_info())


print(emp1.number_of_leaves)
# print(emp2.number_of_leaves)

Employee.update_employee_leaves(21)

# print(emp1.number_of_leaves)
# print(emp2.number_of_leaves)

dev1 = Developer(100, "Jake Coder", "IT-Infra", "Python")
dev2 = Developer(101, "Jenny Coder", "IT-Applications", "Java")

mgr1 = Manager(200, "Bob M", "IT-Infra", [dev2])
mgr2 = Manager(201, "Meg M", "IT-Applications", [dev1])


print(mgr1.print_all_employees())
print(dev1.number_of_leaves)
print(mgr2.number_of_leaves)
