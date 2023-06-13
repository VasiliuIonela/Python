# #Ex_1 - În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
# # variabila = valoare salvata intr-o zona de memorie
#
# #Ex_2 - Declară și inițializează câte o variabilă din fiecare din următoarele tipuri:int, string, float, booleanvarsta = 30
# nume = 'Ionela' # string
# varsta = 30 # int
# salariu= 3000.15 #float
# permis = False # boolean
#
# #Ex_3 - Utilizează funcția type pentru a verifica dacă variabilele declarate mai sus au tipul de date așteptat.
# print(type(nume))
# print(type(varsta))
# print(type(salariu))
# print(type(permis))
#
# #Ex_4 - Rotunjește variabila ‘float’ folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere), apoi verifică din nou tipul de date al acesteia.
# salariu = round(salariu)
# print(salariu)
# print(type(salariu))
#
# #Ex_5 - Incearca sa convertesti variabila string la int folosind type casting si observa rezultatele
# numar = '12134'
# #print(int(nume)) eroare deoarece este un sir de caractere, nu se poate converti in numar: invalid literal for int() with base 10: 'Ionela'
# print(numar)
# numar = int(numar)
# print(type(numar))
#
# #Ex_6 - Incearca sa convertesti variabila boolean la int folosind type casting si observa rezultatele
# print(int(permis))
#
# #Ex_7 - Schimba valoarea variabilei boolean (din true in false sau din false in true) si repeta exercitiul anterior
# permis = True
# print(int(permis))
#
# numar1 = 0
# numar2 = 1
# print(bool(numar1))
# print(bool(numar2))
#
# #Ex_1 -  Folosește funcția print() și printează în consola 4 propoziții folosind cele 4 variabile.
# # Rezolvă nepotrivirile de tip pe rand prin toate modalitatile cunoscute
# print(f'Numele meu este: {nume}. Am varsta de {varsta} ani. Am salariul de: {salariu} ron. Permis de conducere: {permis}.')

# #Ex_2 - Citește de la tastatură numele și prenumele unei persoane și salveaza-le in cate o variabila.
# # Afișează pe ecran următoarea propoziție: 'Numele complet are x caractere'.
# nume = input('Introduceti numele: ')
# prenume = input('Introduceti prenumele: ')
# print(f'numele complet are {len(nume+prenume)}')


#Ex_3 - Citește de la tastatură lungimea și lățimea unui dreptunghi și salveaza-le in cate o variabila.
# Afișează pe ecran următoarea propoziție: 'Aria dreptunghiului este x'.
# lungime = int(input('Introduceti lungimea: '))
# latime =  int(input('Introduceti latimea: '))
# x= lungime * latime
# print(f'Aria dreptunghiului este: {x}')

#Ex_4 - Având stringul: 'Coral is either the stupidest animal or the smartest rock' afișează de câte ori apare cuvântul 'the' în acest string
# text = 'Coral is either the stupidest animal or the smartest rock'
# print(text.count('the'))
#
# #EX_5 Folosindu-te de string-ul de la exercițiul 8, inlocuieste “the” cu “THE” peste tot (inclusiv in cuvantul “either”) si afișează pe ecran rezultatul
# print(text.replace('the', 'THE'))
#
# #Ex_6 Folosindu-te de string-ul de la exercițiul 8 foloseste un assert ca să verifici dacă acest string conține doar numere.
# assert text.isnumeric(), f'textul nu este format doar din numere'

# #Ex_1 Citește de la tastatură un string de dimensiune impară și afișează caracterul din mijloc.
# text = input('Introduceti textul de dimensiune impara: ')
# print(len(text))
# print(text[int(len(text)/2)])

#Ex_2 Folosind assert, verifică dacă un string este palindrom.
# palindrom = 'copaci'
# print(palindrom[::-1])
# assert palindrom == palindrom[::-1], 'nu este un palindrom'

#Ex_3 - Citește un string de la tastatură (ex: 'alabala portocala') asupra caruia sa efectuezi urmatoarele:

# salvează fiecare cuvânt într-o variabilă;
# printează ambele variabile pentru verificare.

# text = input('Introduceti textul: ')
# # text1, text2 = text.split(' ')
# # print(text1, text2)
#
# #Ex_4 - Citește un string de la tastatură (ex: alabala portocala) asupra caruia sa efectuezi urmatoarele:
# # salvează primul caracter într-o variabilă
# # capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.
# primul_caracter = text[0]
# print(primul_caracter + text[1:len(text)-1].replace(primul_caracter, primul_caracter.upper()) + text[-1])

#Ex_5 - citeste un user de la tastatura, citeste o parola. Afiseaza: 'Parola pt user x este ***** si are x caractere
# user = input('Introduceti user: ')
# parola = input('Intorduceti parola: ')
# print(f'Parola pentru {user} este {len(parola)*"*"} si are {len(parola)} caractere')

#Ex_1 Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else
#flow control: codul din interiorul if-ului se executa doar daca conditia if-ului este adevarata. Altfel, se trece in
#ramura de else, daca aceasta exista

#Ex_2 Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural daca este numar intreg mai mare ca 0)
# x = 8.9
# if x >= 0 and isinstance(x, int): # verifica tipul de date al lui x sa fie int
#     print(f'{x} Este un numar natural')
# else:
#     print(f'{x} nu este natural')

#Ex_3 Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
# x = -4
# if x > 0:
#     print(f'{x} este pozitiv')
# elif x == 0:
#     print(f'{x} este neutru')
# else:
#     print(f'{x} este negativ')

#Ex_3 Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).
# x =-2
# if x >= -2 and x <= 13:
#     print(f'{x} se afla in  intervalul -2 si 13')
# else:
#     print(f'{x} este in afara intervalului -2 si 13')

#Ex_4 Verifica daca x NU este intre 5 si 27, excluzand capetele de interval. (a se folosi ‘not’)
# x =27
# if not(x>5 and x<27):
#     print(f'{x} nu se afla in acest interval: 5 si 27')
# else:
#     print(f'{x} se afla in acest interval')

#Ex_5 Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale, daca nu, afiseaza care din ele este mai mare
x = 7
y = 7
if x ==y:
    print('numerele sunt egale')
elif x > y:
    print(f'{x} este mai mare decat {y}')
else:
    print(f'{y} este mai mare decat {x}')

#Ex_6 Presupunand ca x, y, z (toate de tip int) reprezinta laturile unui triunghi, afiseaza
# # daca triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau oarecare (nicio latura nu e egala).
# x = 3
# y = 5
# z = 4
# if x == y and x == z:
#     print('Triunghiul este echilateral')
# elif x == y or x == z or y == z:
#     print('Triungiul este isoscel')
# else:
#     print('Este un triunghi oarecare')

#Ex_7 Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu.
# Atentie! Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.
litera = input('Introduceti litera: ')
if litera in 'AEIOUaeiou':
    print(f'{litera} este vocala')
else:
    print(f'{litera} este o consoana')

















