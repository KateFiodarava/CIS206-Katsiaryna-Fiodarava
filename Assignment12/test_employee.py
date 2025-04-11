from employee import Employee


emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
emp2 = Employee("Mark Jones", 39119, "IT", "Programmer")
emp3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")


employees = [emp1, emp2, emp3]

for emp in employees:
    print("Name:", emp.get_name())
    print("ID Number:", emp.get_idNumber())
    print("Department:", emp.get_department())
    print("Position:", emp.get_position())
    print("-" * 30)
