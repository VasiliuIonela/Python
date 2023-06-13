# 1.ne identificam in platforma angajatorului prin user si parola
# 2.consultam salariul angajatului
# 3.cerem un avans care nu poate depasi 50% din salariul angajatului

user = 'Ion'
parola ='verificare'
salariu = 5000.80
angajat = input('Introduceti numele angajatului: ')
parola_introdusa = input('Introduceti parola: ')
print('Datele au fost introduse, verificam datele')
assert user == angajat, f'Error, expected result: {user}'
assert parola == parola_introdusa, f'Error, expected result: {parola}'
print(f'Salariul lui {user} este de {salariu} lei')
avans = float(input('Introduceti valoarea avansului dorit: '))
print(type(avans))

assert avans == salariu/2, f'Error, expected result: {salariu/2}'

