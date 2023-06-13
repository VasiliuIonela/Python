'''Joc de noroc
Cauta pe net si vezi cum se genereaza un numar random
Imagineaza-ti ca dai cu zarul si salvezi acest numar intr-o variabila numita dice_roll. Numarul salvat va fi
generat random cu metoda gasita in online
Introdu un numar de la tastatura care sa reprezinte numarul ales de la utilizator
Verifica si afiseaza daca utilizatorul a ghicit numarul
Vor exista 3 optiuni care vor trebui tratate:
Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
Ai ghicit. Felicitari? Ai ales x si zarul a fost y'''
import random
while True:
    dice_roll = random.randint(1,6)
    guess = int(input('Introduceti numarul: '))
    if guess == dice_roll:
        print(f'Ai ghicit. Felicitari. Ai ales {guess} si zarul a fost {dice_roll}')
        break
    elif guess > dice_roll:
        print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {guess} dar a fost {dice_roll}')
    else:
        print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {guess} dar a fost {dice_roll}')

'''
scrieti un program in python prin care sa verificati daca un numar introdus de la tst este multiplu de 5 va afisa buzz.
Altfel, daca este multiplu de 3 va afisa fizz.
Daca este multiplu si de 3 si de 5, se va afisa fizz buzz.
'''
# numar = int(input('Introduceti nr: '))
# if numar % 5 ==0 and numar % 3 == 0:
#     print('fizzbuzz')
# elif numar %3 == 0:
#     print('fizz')
# elif numar % 5 == 0:
#     print('buzz')
# else:
#     print(numar)

'''
Vrem sa cream o aplicatie pentru achizitionare bilete de avion care sa primeasca drept inputuri urmatoarele informatii:
Varsta
insotit de ambii parinti
Pasaport
act permisiune parinte lipsa
#
Conditii de imbarcare:
Daca pers are varsta peste 18 ani si are pasaport
Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si 
are permisiune in scris de la celalat parinte
#
Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l cu toate variantele care
 crezi ca ar trebui testate.
Genereaza scenarii de testare cu expected results si apoi ruleaza codul pentru a verifica daca 
expected results sunt egale cu actual results.
#
Exemple:
Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca

Scenarii de testare:
Adult peste 18 ani cu pasaport valid => Se poate imbarca
Adult peste 18 ani cu pasaport invalid => Nu se poate imbarca
Copil cu pasaport valid si ambii parinti => Se poate imbarca
Copil cu pasaport valid si un singur parinte - permisiune parinte lipsa => Se poate imbarca
Copil cu pasaport valid si un singur parinte - fara permisiune parinte lipsa => Nu se poate imbarca
Copil fara pasaport valid => Nu se poate imbarca
'''
# varsta = int(input('Introduceti varsta:'))
# pasaport = input('E pasaportul valid? da/nu')
#
# if varsta >= 18  and pasaport == 'da':
#     print('Va puteti imbarca')
# elif varsta < 18  and pasaport == 'da':
#     insotit_de_ambii_parinti = input('Este insotit de ambii parinti? da/nu')
#     if insotit_de_ambii_parinti == 'da':
#         print('Va puteti imbarca')
#     else:
#         act_permisiune = input('Are permisiunea de la parintele lipsa? da/nu')
#         if act_permisiune == 'da':
#             print('Va puteti imbarca')
#         else:
#             print('Nu va puteti imbarca')
# else:
#     print('Nu va puteti imbarca')




