#listele pot sa cuprinda dif tipuri de elemente si sunt dinamice
fructe=['mar', 'banana', 'portocala', 1, True]
#afisam o lista
print(fructe)

#accesam un element in functie de index
print(fructe[0])
#adaugam un element in lista
fructe.append('rosie')
#suprascriere
fructe[0]='para'
print(fructe)
#dimensiunea
print(len(fructe))

#scoate si ne returneaza ultimul element
last = fructe.pop()
print(f'ultimul element:  {last}')
print(f'lista:  {fructe}')
# de cate ori apare un element
print(fructe.count(1))
#extindem lista/unim doualiste
fructe_exotice=['ananas', 'kiwi']
fructe.extend(fructe_exotice)
print(fructe)