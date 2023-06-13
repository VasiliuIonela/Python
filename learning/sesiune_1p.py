# 1.ne identificam in platforma angajatorului prin user si parola
# 2.consultam salariul angajatului
# 3.cerem un avans care nu poate depasi 50% din salariul angajatului
# 4.adaugam un moto personal
# 5.adaugam un nou angajat: Maria, parola: 112222, salariu 5100.0

user = 'Ion'
parola ='verificare'
salariu = 5000.80
ang = True
motto_personal = 'Singura diferenta intre o zi buna si una rea este atitudinea ta'

user1 = 'Maria'
parola1 = 1234
ang1 = False
salariu1 = 5100.0
motto_Maria = 'nu exista lift care sa te duca la succes, trebuie sa folosesti scarile'

if not(salariu1 >= 5000.0 and ang1):
    print(f'{user1}')
if salariu >= 5000 and ang:
    print(f'{user}')

lista_motto =motto_Maria.split(" ")
print(lista_motto)
numara_a = motto_Maria.count('a')
print(f'Numarul de a-uri din fraza este: {numara_a}')
print(motto_Maria.capitalize())


'''angajat = input('Introduceti numele angajatului: ')
if angajat == user:
        parola_introdusa = input('Introduceti parola: ')
        if parola_introdusa == parola:
            print(f'Bine ai venit, {user}')
            print(f'Motto-ul lui {user} este: {motto_personal}')
        else:
            print('Parola introdusa este gresita')

elif angajat == user1:
    parola_introdusa = int(input('Introduceti parola: '))
    if parola_introdusa == parola1:
        print(f'Bine ai venit, {user1}')
        print(f'Motto-ul lui {user1} este: {motto_Maria}')
        print(f'{motto_Maria[::2]}')
        print(f'{motto_Maria[::-1]}')
    else:
        print('Parola introdusa este gresita')
'''









