#creare de variabile
nume = 'Popescu Ion'
an_nastere= 1993
salariu = 5000.35
angajat =True

#tipurile de date
print(type(nume))
print(type(an_nastere))
print(type(angajat))
print(type(salariu))

#type casting
print(str(an_nastere))

#concatenare prin formatare
print(f'{nume} este nascut in anul {an_nastere} si este un angajat:  {angajat} cu un salariu de {salariu}')
#concatenare prin type casting
print(nume + " este nascut in anul " + str(an_nastere) + " si este angajat cu un salariu de " + str(salariu) + " lei")

#assert
assert an_nastere == 1993
assert angajat == True, f'Error, valoarea obtinuta nu e corecta. Expected: True, actual: {angajat}'

#functia input() -luam date de la tst
nume_angajat = input('Va rugam sa introduceti un nume: ')


