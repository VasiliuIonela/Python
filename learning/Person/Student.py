from learning.Person.Person import Person
class Student(Person):
    def __init__(self, name, age, adress, faculty, year_of_study):
        super().__init__(name, age, adress)
        self.faculty = faculty
        self.year_of_study = year_of_study
    def description(self):
        super().description()
        print(f'I study at {self.faculty}, year of study: {self.year_of_study}.\n')
