from learning.Person.Employee import Employee
class SoftwareEngineer(Employee):
    def __init__(self, name, age, adress, company, salary, years_of_experience):
        super().__init__(name, age, adress, company, salary)
        self.years_of_experience = years_of_experience
    def description(self):
        super().description()
        print(f'Experience: {self.years_of_experience} years')