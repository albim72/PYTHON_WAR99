class Department:
    def __init__(self,name,employees):
        self.name = name
        self.employees = employees


class Employee:
    def __init__(self,name,department):
        self.name = name
        self.department = department

department = Department("IT",[])
employee1 = Employee("Olga Nowak",department)
employee2 = Employee("Adam Kot",department)
employee3 = Employee("Lidia Kowal",department)

department.employees.append(employee1)
department.employees.append(employee2)
department.employees.append(employee3)

print(department.name)
print(f'liczba pracowników działu: {len(department.employees)}')
print("Pracownicy: ")
print(department.employees[0].name)
print(department.employees[1].name)
print(department.employees[2].name)

