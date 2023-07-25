#tema:
#cautati cate caractere dintr-un cuvant sunt nepotrivite, sa le eliminati,
#intrebati userul daca vrea sa primeasca definitia noului cuvant. in caz ca nu exista in dictionar,
# sa ii cerem userului adaugarea definitiei lui.
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
        return cuvant
    else:
        cuv_nou = ''
        nr_caractere_nepotrivite = 0
        for caracter in cuvant:
            if caracter.isalpha():
                cuv_nou += caracter
            else:
                nr_caractere_nepotrivite += 1
        return cuv_nou
def printeaza_definitia(dict, cuvant):
    cuv_nou = este_cuvant_valid(cuvant)
    if cuv_nou in dict.keys():
        mesaj = input(f'Vreti sa vedeti definitia cuvantului? da/nu: ')
        if mesaj == 'da':
            print(f'\n{cuv_nou}:{dict[cuv_nou]}')
        else:
            print('Nu, multumesc.')
def consulta_cuvant(dict, cuvant):
    cuv_nou = este_cuvant_valid(cuvant)
    if cuvant in dict.keys():
        print(f'{cuvant}: {dict[cuvant]}')
    elif cuv_nou in dict.keys():
        print(f'Forma corecta a cuvantului este: {cuv_nou}.\n')
        printeaza_definitia(dict, cuv_nou)
    else:
        definitie = input(f"Forma corecta a cuvantului introdus este {cuv_nou}.\nCuvantul nu exista in dictionar, va rugam introduceti definitia: ")
        dict[cuv_nou] = definitie
        print(f'{cuv_nou}: {dict[cuv_nou]}')
consulta_cuvant(dict, cuvant)