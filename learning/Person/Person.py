import datetime
class Person:
    def __init__(self, nume, varsta, adresa):
        self.nume =nume
        self.varsta=varsta
        self.adresa =adresa
    def description(self):
        print('*'*50)
        print(f'My name is {self.nume}, age of:{self.varsta} years, I live at the adress: {self.adresa}.\n')
    def birth_year(self):
        currentyear= datetime.date.today().year
        return currentyear-self.varsta
