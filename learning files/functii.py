def printGreeting():
    print('buna ziua')

def printGreetingbyName(nume, prenume):
    print(f'buna ziua, {nume} {prenume}')

def mediaNr(a, b, c):
    return (a+b+c)/3

def piValue():
    return 3.14

# daca pers e majora return true altfel false
def verifMajor(varsta):
    if varsta>=18:
        return True
    else:
        return False
def nrMare(a,b):
    if a>b:
        return a
    else:
        return b

#zona de apelare
printGreeting()
printGreetingbyName('ionela','vasiliu')
printGreetingbyName('radu','vasiliu')
printGreetingbyName('david','vasiliu')
printGreetingbyName('adam','vasiliu')
print(mediaNr(3,4,3))
print(piValue())

print(verifMajor(20))
print(verifMajor(15))

age=int(input('introduceti varsta:'))
if verifMajor(age):
    print('persoana este majora')
else:
    print('persoana este minora')

print(nrMare(3,4))