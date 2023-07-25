from learning.Person.Person import Person
from learning.Person.Student import Student
from learning.Person.Employee import Employee
from learning.Person.SoftwareEngineer import SoftwareEngineer
if __name__=='__main__':
    person1= Person('Ionela', 30, 'Iasi')
    person1.description()
    student1= Student('Ion', 21, 'Iasi', 'Biology Faculty', 2010)
    student1.description()
    employee1=Employee('Dan', 32, 'Cluj', 'Centric', 2000)
    employee1.description()
    print(f'salariul anual: {employee1.annual_salary()}')
    employee2=SoftwareEngineer('Dan', 32, 'Cluj', 'Centric', 2000, 4)
    employee2.description()
