from learning.Person.Person import Person
class Employee(Person):
    def __init__(self, name, age, adress, company, salary):
        super().__init__(name, age, adress)
        self.company=company
        self.salary=salary
    def description(self):
        super().description()
        print(f'I work at {self.company} company, and I have my salary: {self.salary} euro')
    def annual_salary(self):
        return self.salary *12
