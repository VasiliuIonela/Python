#dalmatieni
for  i in range(1,102):
    print(f'dalmatinaul cu numarul: {i}')
    #din 2 in 2
    for i in range(1,102, 2):
        print(f'dalamtianul cu nr {i}')
# for
#parcurgere lista prin index
numere =[3, 7, 10, 30]
'''
for i in range(0, len(numere)):
    print(f'indexul este : {i}')
    print(f'numarul este: {numere[i]}')
'''
'''
# for each
for numar in numere:
    print(f'numarul curent este: {numar}')
    s=s+numar
print(f'suma este: {s}')'''

#de cate ori apare 3 in [3, 2, 3, 5, 3]

sir_numere=[3,2,3,5,3]
print(sir_numere)
nr=0
for numar in numere:

    if numar==3:
        nr+=1;
        print(f'numarul 3 se gaseste de {numar} ori in lista')
