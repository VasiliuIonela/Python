'''
Calculare pret discount

Dacă un client are peste 65 de ani, atunci i se va oferi o reducere de 15%.
În caz contrar, dacă clientul nu are peste 65 de ani, dacă persoana călătorește cu cel puțin un copil va avea o reducere de 10%
Atat pentru seniori cat si pentru non- seniori se va aplica o reducere suplimentara de 10% daca vor calatori in timpul iernii.
De asemenea, atât pentru seniori, cât și pentru non seniori se va aplica o taxă de lux de 3% dacă vor călători în clasa I (în orice sezon) sau 1% taxă de gestiune în caz contrar.

'''
# varsta =int(input('Introduceti varsta clientului: '))
# pret_bilet = 400.0
# discount = 0
# copil =False
# iarna = True
# clasa1 = True
# taxa = 0
# if varsta > 65:
#     discount += 15
# elif copil == True:
#     discount += 10
# if iarna == True:
#     discount += 10
# if clasa1 == True:
#     taxa +=3
# else:
#     taxa+=1
# pret_final = pret_bilet - (pret_bilet*discount/100)+ pret_bilet*taxa/100
# print(pret_final)
'''
Calculare discount seller

Compania X vinde mărfuri la punctele de vânzare cu ridicata și cu amănuntul. 
Clienții angro primesc o reducere de două procente la toate comenzile. 
De asemenea, compania încurajează atât clienții angro, cât și clienții cu amănuntul să plătească ramburs la livrare, 
oferind o reducere de două procente pentru această metodă de plată. 
Încă o reducere de două procente este acordată pentru comenzile de 50 sau mai multe unități.
'''
# discount = 2
# plata_ramburs = True
# client_angro = True
# if client_angro:
#     discount +=2
# if plata_ramburs:
#     discount += 2
# suma = 2000
# pret_final = suma - (suma*discount/100)
# print(pret_final)

#Introduceti un nume de film de la tastatura si evaluati daca numele acelui film este numele filmului vostru preferat.
# Daca da, atunci printati pe ecran: “Acesta este filmul meu preferat”.
# In caz contrar printati pe ecran: “Din pacate nu este filmul meu preferat”
# film =  input('Introduceti numele filmului: ')
# preferat = 'Shutter Island'
# if film.upper() == preferat.upper():
#     print('Acesta este filmul meu preferat')
# else:
#     print('Din pacate nu este filmul meu preferat')

#Aveti la dispozitie urmatorul database url:
# jdbc:mysql://mysql.db.server:3306/my_database?useSSL=false&serverTimezone=UTC
#Extrageti din acest text numele bazei de date: mysql.db.server
#Folositi un if statement pentru a evalua daca numele bazei de date este cel corect
# (presupunand ca extrageti url-ul dintr-un sistem extern si nu stiti care este acesta)
text ='jdbc:mysql://mysql.db.server:3306/my_database?useSSL=false&serverTimezone=UTC'
nume ='mysql.db.server'
if nume in text:
    print('Numele bazei de date este corect')
else:
    print('Eroare. URL incorect')

