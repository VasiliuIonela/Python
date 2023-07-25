# print('Bine ati venit la dictionar 1.0')
# cuvant = input('Introduceti un cuvant:\n')
# dict = {}
# print(f'Vom accesa dictionarul: {dict[cuvant]}')

# print('Bine ati venit la dictionar 1.1')
# cuvant = input('Introduceti un cuvant:\n')
# dict = {}
# try:
#     print(f'Vom accesa dictionarul: {dict[cuvant]}')
# except:
#     print(f'Ne pare rau, cuvantul {cuvant} nu a fost gasit in dictionar.')


#vom da optiunea userului ca atunci cand cere un cuvant care nu exista in dict, sa il adauge el
# print('Bine ati venit la dictionar 1.2')
# cuvant = input('Introduceti un cuvant:\n')
# dict = {
#     "apa" : " Lichid incolor, fără gust și fără miros, compus hidrogenat al oxigenului, care formează unul dintre învelișurile Pământului.",
#     "pamant" : "Scoarța globului terestru, partea de uscat a globului terestru; suprafața lui (împreună cu atmosfera) pe care trăiesc oamenii și alte vietăți.",
#     "zebra" : "Nume generic dat speciilor de cai sălbatici africani cu blana vărgată cu benzi alternative, deschise și închise; animal care face parte din aceste specii"
# }
# if cuvant in dict.keys():
#     print(f'{cuvant}: {dict[cuvant]}')
# else:
#     definitie = input("cuvantul nu exista. va rugam introduceti definitia.\n")
#     dict[cuvant] = definitie
# print(dict)

# print('Bine ati venit la dictionar 1.3')
# cuvant = input('Introduceti un cuvant:\n')
# dict = {
#     "apa" : " Lichid incolor, fără gust și fără miros, compus hidrogenat al oxigenului, care formează unul dintre învelișurile Pământului.",
#     "pamant" : "Scoarța globului terestru, partea de uscat a globului terestru; suprafața lui (împreună cu atmosfera) pe care trăiesc oamenii și alte vietăți.",
#     "zebra" : "Nume generic dat speciilor de cai sălbatici africani cu blana vărgată cu benzi alternative, deschise și închise; animal care face parte din aceste specii"
# }
# def consulta_cuvant(cuvant, dict):
#     if cuvant in dict.keys():
#         print(f'{cuvant}: {dict[cuvant]}')
#     else:
#         definitie = input("cuvantul nu exista. va rugam introduceti definitia.\n")
#         dict[cuvant] = definitie
# consulta_cuvant(cuvant, dict)

# print('Bine ati venit la dictionar 1.4')
# #cuvant = input('Introduceti un cuvant:\n')
# dict = {
#     "apa" : " Lichid incolor, fără gust și fără miros, compus hidrogenat al oxigenului, care formează unul dintre învelișurile Pământului.",
#     "pamant" : "Scoarța globului terestru, partea de uscat a globului terestru; suprafața lui (împreună cu atmosfera) pe care trăiesc oamenii și alte vietăți.",
#     "zebra" : "Nume generic dat speciilor de cai sălbatici africani cu blana vărgată cu benzi alternative, deschise și închise; animal care face parte din aceste specii"
# }
# def consulta_cuvinte(dict, *args):
#     for cuvant in args:
#         if cuvant in dict.keys():
#             print(f'{cuvant}: {dict[cuvant]}')
#
# consulta_cuvinte(dict,'albastru', 'zebra')

#print('Bine ati venit la dictionar 1.5')
#tratam cazul in care userul introduce un cuvant gresit
# cuvant = input('Introduceti un cuvant:\n')
# dict = {
#     "apa" : " Lichid incolor, fără gust și fără miros, compus hidrogenat al oxigenului,
#     care formează unul dintre învelișurile Pământului.",
#     "pamant" : "Scoarța globului terestru, partea de uscat a globului terestru;
#     suprafața lui (împreună cu atmosfera) pe care trăiesc oamenii și alte vietăți.",
#     "zebra" : "Nume generic dat speciilor de cai sălbatici africani cu blana vărgată cu benzi alternative,
#     deschise și închise; animal care face parte din aceste specii"
# }
# def consulta_cuvant(dict, cuvant):
#     if cuvant in dict.keys():
#         print(f'{cuvant}: {dict[cuvant]}')
#     else:
#         print(f'Ne pare rau, cuvantul {cuvant} nu exista')
# def este_cuvant_valid(cuvant):
#     if cuvant.isalpha():  # functie folosita sa verificam daca cuvantul contine caractere alfabetice
#         print(f'cuvantul {cuvant} este valid')
#     else:
#         raise Exception(f'Acest cuvant {cuvant} este incorect scris')
# este_cuvant_valid(cuvant)
# consulta_cuvant(dict, cuvant)



#tema:
# cautati cate caractere dintr-un cuvant sunt nepotrivite, sa le eliminati,
# si sa intrebati userul daca vrea sa adauge cuvantul in dictionar
#.apa este invalid, apa3 este invalid. a.p.a este invalid

print('Bine ati venit la dictionar 1.6')
cuvant = input('Introduceti un cuvant:\n')
dict = {
     "apa" : " Lichid incolor, fără gust și fără miros, compus hidrogenat al oxigenului, "
             "care formează unul dintre învelișurile Pământului.",
     "pamant" : "Scoarța globului terestru, partea de uscat a globului terestru; "
                "suprafața lui (împreună cu atmosfera) pe care trăiesc oamenii și alte vietăți.",
     "zebra" : "Nume generic dat speciilor de cai sălbatici africani cu blana vărgată cu benzi alternative, "
               "deschise și închise; animal care face parte din aceste specii"
 }
def este_cuvant_valid(cuvant):
    if cuvant.isalpha():
        #print(f'{cuvant} este un cuvant valid')
        return cuvant
    else:
        #print(f'{cuvant} nu este valid')
        cuv_nou = ''
        nr_caractere_nepotrivite = 0
        for caracter in cuvant:
            if caracter.isalpha():
                cuv_nou += caracter
            else:
                nr_caractere_nepotrivite += 1
        #print(f'Numarul de caractere non-alpha din {cuvant} este egal cu: {nr_caractere_nepotrivite}')
        #print(f'Forma corecta a cuvantului {cuvant} este: {cuv_nou}')
        return cuv_nou
print(f"forma corecta a cuvantului introdus este: {este_cuvant_valid(cuvant)}")
def consulta_cuvant(dict, cuvant):
    if cuvant in dict.keys():
        print(f'{cuvant}: {dict[cuvant]}')
    else:
        definitie = input("Cuvantul nu exista. va rugam introduceti definitia.\n")
        dict[este_cuvant_valid(cuvant)] = definitie
        print(dict)
consulta_cuvant(dict, cuvant)

#daca vrem sa printam toate cuvinetele din dict, folosind parametrul **kwargs
print('Bine ati venit la dictionar 1.7')
def afiseaza_dict(**kwargs):
    for cuvant, definitie in kwargs.items():
        print(f"{cuvant}: {definitie}")
dict = {
     "apa" : " Lichid incolor, fără gust și fără miros, compus hidrogenat al oxigenului, "
             "care formează unul dintre învelișurile Pământului.",
     "pamant" : "Scoarța globului terestru, partea de uscat a globului terestru; "
                "suprafața lui (împreună cu atmosfera) pe care trăiesc oamenii și alte vietăți.",
     "zebra" : "Nume generic dat speciilor de cai sălbatici africani cu blana vărgată cu benzi alternative, "
               "deschise și închise; animal care face parte din aceste specii"
}
afiseaza_dict(**dict)

