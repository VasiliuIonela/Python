# liste
print('-------------------- LISTE -------------------- ')
lista1 = ['a', 2, 3, 1]
lista2 = list(('a', 2, 3, 5))
print(lista1, type(lista1))
print(lista2, type(lista2))
#cum accesam primul element din lista?
x = lista1[0]
print(x)

# cum accesam ultimul element din lista?
y = lista1[-1]
print(y)

#cum aflam dimensiunea unei liste?
print(len(lista1))

# cum adaugam un element la sfarsitul listei
lista1.append('b')
print(lista1)

#cum adaugam un element pe o pozitie oarecare folosind functia insert
lista1.insert(1, 'c')
print(lista1)

#cum stergem un element din lista
lista1.remove(3)
print(lista1)

#cum recuperam si scoatem din lista ultimul element
z = lista1.pop()
print(z)
print(lista1)

# cum duplicam/triplicam o lista
lista2 *= 3
#lista2 = lista2 * 3
print(lista2)

print('-------------------- SETS -------------------- ')
# neordonate, nu contin elemente repetate, sunt mutabile
set1 = {1, 2, 3, 'a'}
set2 = set((1, 2, 3, 'b'))
print(set1, type(set1))
print(set2, type(set2))

# adaugam un element in set
set2.add(4)
print(set2)

set2.add(3)
print(set2)
#cum obtinem un element oarecare din set
z = set2.pop()
print(set2, z)
#cum stergem un element din set
set2.remove(3)
print(set2)

print('-------------------- TUPLES -------------------- ')
# imutabile
tuple1 = (1, 2, 3, 'b', 'C')
tuple2 = tuple((1, 2, 3, 'b', 'c'))
print(tuple1, type(tuple1))
print(tuple2, type(tuple2))

#cum aflam elementul de pe pozitia 2 din tupla
print(len(tuple2))
print(tuple2[2])
#cum adaugam un element intr-o tupla
#tuple1.add(4) -eroare, nu se pot adauga elemente in tupla
#cum se creaza o tupla din mai multe tuple
#print(tuple1.__add__(tuple1, tuple2))

print('-------------------- DICTIONARIES -------------------- ')
# sunt mutabile, neordonate, au chei unice
dict1 ={'d': 1, 'e': 2, 'f': 3,'d':4}
dict2 = dict(a=1, b=2, c=3)
print(dict1, type(dict1))
print(dict2, type(dict2))

d = len(dict1)
print(d)
# actualizare valoare
dict2.update({'b':66})
print(dict2)
#adauga o pereche cheie-valoare
dict2.update({'d': 4})
print(dict2, len(dict2))
# actualizare valoare in dict2 fara a ne folosi de functia update
dict2['d'] = '53'
print(dict2)
#stergere valoare din dict
del dict2['b']
print(dict2)

x2 = dict2.pop('d')
print(dict2)
print(x2, type(x2))

#cum cream o lista care sa contina cele 2 dictionare
multilist = [dict1, dict2]
print(multilist, type(multilist))
multilist.append(tuple1)
multilist.append(tuple2)
print(multilist, type(multilist))

# cum adaugam set1 si set2 la multilist fara sa folosim functia append
multilist2 = [multilist, set1, set2]
print(multilist2)
print(type(multilist2), type(multilist2[0]), type(multilist2[1]))
