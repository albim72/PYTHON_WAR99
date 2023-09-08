class Address:
    def __init__(self,street,city,country):
        self.street = street
        self.city = city
        self.country = country

class Person:
    def __init__(self,name,address):
        self.name = name
        self.address = address

class Employee:
    def __init__(self,name,address,employee_id):
        self.person = Person(name,address)
        self.employee_id = employee_id

address = Address("Złota 6/4 12-567","Kraków","Polska")
employee = Employee("Jan Kot",address,45345)

print(employee.person.name)
print(employee.person.address.city)
print(employee.employee_id)
