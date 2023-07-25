print('---------FOR---------')
suma1 = 0
list_impare = []
for i in range(0, 11):
    if i % 2 == 0:
        continue
    list_impare.append(i)
    suma1 += i
print(f'Numerele impare sunt: {list_impare} iar suma acestora este: {suma1}')
print('---------WHILE---------')

i = 11
while i > 0:
    i -= 1
    if i == 3:
        continue
    print(i)

print('---------FOR---------')
#vrem sa numaram cat cifre se impart exact la 7 intre 1 si 100
cate_nr_exact_la7 = 0
list_7 =[]
for numar in range(1,101):
    if numar % 7 == 0:
        cate_nr_exact_la7 +=1
        list_7.append(numar)
print(f'Avem {cate_nr_exact_la7} numere care se impart exact la 7, acestea sunt:  {list_7}')
print('---------FOR EACH---------')
#parcurgem list 7, ridicam la patrat fiecare element, scadem 3, lasam rezultatul intr-o noua lista
lista_noua =[]
for numar in list_7:
    numar_calculat = numar ** 2 - 3
    lista_noua.append((numar_calculat))

print(f'Lista obtinuta  este: {lista_noua}')
list_7.pop()

if len(list_7) == len(lista_noua):
    print('Listele au dimensiuni egale')
else:
    print(f'listele nu au dim egale: {len(list_7)}, {len(lista_noua)}')

#programul sa numere cate vocale avem intr-un sir de caractere foarte lung
sir ='programul sa numere cate vocale avem intr-un sir de caractere foarte lung'
nr_vocale = 0
for caracter in sir:
    if caracter in 'aeiou':
    #if caracter == 'a' or caracter == 'e' or caracter =='i' or caracter =='o' or caracter =='u':
        nr_vocale+=1
print(nr_vocale)

# un program care sa imprime tabla inmultirii

for i in range(1,11):
    for j in range(1,11):
        print(f'{i}*{j} = {i*j}')
    print()

