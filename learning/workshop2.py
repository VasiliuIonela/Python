# #1. Declarati o lista cu elemente multitype
# list1 = [1, 'ITF', 99, 3.14, True]
# #2. Declarati o lista goala
# list2 =[]
# list2= list()
# #3. Accesati orice element din lista pe baza de index
# print(list1[0])
#
#
# #4. Accesati pozitia unui element din lista pe baza functiei index()
# elem = list1.index(3.14)
# print(elem)
# elem_index_inexistent = list1.index(10) #ValueError: 10 is not in list
# 5. Adaugati elemente in lista atat cu functia append() cat si cu functia insert().
# Observati rezultatele

# list1 = [1, 'ITF', 99, 3.14, True]
# list2 = [1, 2, 3, 4]
# list1.append(list2)
# print(list1)
# print(list1[5])
# list1.insert(2, list2)
# print(list1)
# list1.insert(4, 'gov')
# print(list1)
# #6. Stergeti elemente din lista atat cu functia pop() cat si cu functia remove(). Observati rezultatele
# list1.pop()
# print(list1)
# #sterge elem specificat prin index cu  fct pop
# list1.pop(2)
# print(list1)
# #sterge elem specificat prin valoare cu fct remove
# list1.remove('ITF')
# print(list1)
# #list1.remove('ceva') #ValueError: list.remove(x): x not in list
# #7. Numarati elementele dintr-o lista folosind functia len()
# lungime_lista =len(list1)
# print(lungime_lista)
# #8. Numarati de cate ori apare un anumit element in lista folosind functia count()
# list1.count(1)
# list1.extend(list2)
# print(list1)
# lista3 =[10, 5, 4.5, 30, -2, -7]
# lista3.sort()
# print(lista3)
# lista3.sort(reverse=True)
# print(lista3)
# lista4= ['g', 'gov', 'ana', 'gheo']
# lista4.sort(reverse=True)
# print(lista4)
# lista3.clear()
# print(lista3)
# lista3 =[10, 5, 4.5, 30, -2, -7]
# #12. Parcurgeti o lista si printati toate elementele din aceasta folosind pe
# # rand for, while si foreach
# for index in range(len(lista3)):
#     print(lista3[index], end=' ')
# print()
#
# for numar in lista3:
#     print(numar, end=' ')
#
# print()
#
# i= 0
# while i <len(lista3):
#     print(lista3[i], end= ' ')
#     i +=1
# tupla1 = (5, 'gigi', 3.14, 'Ana', -7)
# tupla2 = tuple()
# print(tupla1)
# print(tupla2)
# tupla4=(9,)
# print(tupla4, type(tupla4))
# print(tupla1.index(3.14))
# print(tupla1.count('gigi'))
# if tupla1.index(3.14)==2:
#     print('da')
# else:
#     print('nu')
# set1={6, -22, 'vali', 44}
# set1.add(55)
# print(set1)
# #set1.add([1, 2, 3]) #TypeError: unhashable type: 'list'
# #set1.pop()
# print(set1)
#
# set1.remove(-22)
# print(set1)
# set1.discard(44)
# print(set1)
# set1= {10,15,30, 4,-7}
# set2={10,15,30}
# print(set2.issubset(set1))
# print(set1.issuperset(set2))
# set2={10,15,30, -20}
# print(set2)
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set2.difference(set1))
# set1.clear()
# set2.clear()
# print(set1,set2)

# dict1={'nume' :'Ionela', 'varsta': 31, 'oras': 'Brasov'}
# dict2={}
# print(dict1)
# dict3= dict()
# print(type(dict2), type(dict3))
# dict1.update({'limba': 'romana'})
# print(dict1)
# dict1['profesia']='instalator'
# print(dict1)
# dict1.update({'profesia': 'zugrav'})
# print(dict1)
# dict1['limba']='engleza'
# print(dict1)
# oras = dict1.get('oras')
# print(oras)
# nume=dict1['nume']
# print(nume)
# # dict1.pop('profesia')
# # # print(dict1)
# # # dict1.popitem()
# # # print(dict1)
# print(dict1.keys())
# print('*'*5, 'chei ', '*'*5)
# for cheie in dict1.keys():
#     print(cheie)
# print('*'*5, 'valori ', '*'*5)
# for valoare in dict1.values():
#     print(valoare)
# print('*'*5, 'cheie: valoare ', '*'*5)
# print(dict1.items())
# for  cheie, valoare in dict1.items():
#     print(cheie, valoare)
# dict1.clear()
# print(dict1)
#Aveti urmatorul dictionar (dictionar imbricat / nested dictionary / embedded dictionary):
# fotbalisti_pe_echipe = {
#     "Barcelona": {
#         "Dica":
#             {
#                 "Nume complet": "Nicolae Dica",
#                 "Varsta": 45,
#                 "Numar Tricou": 10
#             },
#         "Banel":
#             {
#                 "Nume complet": "Banel Nicolita",
#                 "Varsta": 47,
#                 "Numar Tricou": 3
#             },
#         "Dukadam":
#             {
#                 "Nume complet": "Helmut Dukadam",
#                 "Varsta": 65,
#                 "Numar Tricou": 7
#             }
#     }
# }
# # Pe baza acestui dictionar faceti urmatoarele exerciti:
# # Printati pe ecran numarul de pe tricou al oricarui jucator doriti
#
# print(f" Acesta este nr lui Dica: {fotbalisti_pe_echipe['Barcelona']['Dica']['Numar Tricou']}")
# print(fotbalisti_pe_echipe['Barcelona']['Banel']['Numar Tricou'])
# print(fotbalisti_pe_echipe['Barcelona']['Dukadam']['Numar Tricou'])
# # Folositi functia pop pentru a scoate orice jucator din dictionar
# #dukadam = fotbalisti_pe_echipe['Barcelona'].pop('Dukadam')
# # Printati pe ecran detaliile despre fiecare jucator astfel incat sa obtineti urmatorul rezultat:
#
# #print(dukadam)
# print(fotbalisti_pe_echipe)
# for echipa, jucator in fotbalisti_pe_echipe.items():
#     for nume, detalii in jucator.items():
#         print(f'La echipa :{echipa} joaca jucatorul:')
#         for cheie in detalii.keys():
#             print(f"detalii jucator- {cheie}: {detalii[cheie]}", end=",")
#         print()
# for i in range(1, 102):
#     #print(f'Dalmatianul curent se afla la pozitia "{i}"')
#     print(f"Dalmatianul nostru se afla pe pozitia:\"{i}\" ")
#metoda bulelor tema

def bubble_sort(lista):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(lista)-1):
            if lista[i]>lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                sorted = False
def bubble_sort_desc(lista):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(lista)-1):
            if lista[i]<lista[i+1]:
                lista[i], lista[i+1]= lista[i+1], lista[i]
                sorted = False

#lista_mea = [200, 15, 13, 6, 2, 90, 3, 5]
#print(f'Lista initiala este: {lista_mea}' )
# #bubble_sort(lista_mea)
# bubble_sort2(lista_mea)
# print(f'lista sortata crescator este : {lista_mea}')
# bubble_sort_desc(lista_mea)
# print(f'lista sortata descrescator este : {lista_mea}')
# print('--------------------------')
# sir = ['delfin','ana', 'copac', 'alfabet' , 'catalog']
# print(f'sirul meu este: {sir}')
# bubble_sort(sir)
# print(f'sirul sortat crescator este: {sir}')
# bubble_sort_desc(sir)
# print(f'sirul sortat descrescator este: {sir}')
lista_mea = [200, 15, 13, 6, 2, 90, 3, 5]
print(f'Lista initiala este: {lista_mea}' )

sortat = False
while not sortat:
    sortat = True
    for i in range(len(lista_mea)-1):
       if lista_mea[i] > lista_mea[i+1]:
           lista_mea[i], lista_mea[i+1] = lista_mea[i+1], lista_mea[i]
           sortat = False
print(f'lista actuala sortata crescator este : {lista_mea}')
