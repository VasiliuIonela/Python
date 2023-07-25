from learning.Clase.GradinitaPrivata import GradinitaPrivata
from learning.Clase.GradinitaPublica import GradinitaPublica
from learning.Clase.GradinitaPublica25 import GradinitaPublica25
from learning.Clase.GradinitaPublica26 import GradinitaPublica26
from learning.Clase.Prst import Prst
from learning.Clase.Gradinita import Gradinita
if __name__== '__main__':
    #gradinita_privata= GradinitaPrivata()
    # gradinita_privata.ora_de_somn()
    # gradinita_publica = GradinitaPublica()
    # gradinita_publica.activitate_practica()
    # #gradinita=Gradinita() #nu putem sa instantiem clasa abstracta
    # # gradinita_publica25=GradinitaPublica25()
    # # gradinita_publica25.activitate_practica()
    # # gradinita_publica25.ora_de_somn()
    # # gradinita_publica25.calculam_buline()
    # #gradinita_publica25.introduceti_informatii_elevi()
    # gradinita_publica26=GradinitaPublica26()
    # print(f'{gradinita_publica26.atribut_public}')
    # print(f'{gradinita_publica26._atribut_protejat}')
    # print('---------getter----------')
    #
    # print(f'{Prst.BLUE} {gradinita_publica26.atribut_privat} {Prst.RESET}')
    # print('-----------setter---------')
    # gradinita_publica26.atribut_privat = "newValuePrivat"
    # print(f'{Prst.RED} {gradinita_publica26.atribut_privat}{Prst.RESET}')
    # del gradinita_publica26.atribut_privat
    #
    # print(f'{gradinita_publica26.atribut_privat}')
    gradinita_privata = GradinitaPrivata()
    # nume_copil= input('Introduceti numele copilului:\n')
    # varsta_copil= int(input('Introduceti varsta copilului:\n'))
    # an_inscriere= input('Introduceti anul de inscriere:\n')
    # gradinita_privata._adauga_elev(nume_elev= nume_copil, varsta = varsta_copil, an_inscriere=an_inscriere)
    # print(gradinita_privata.informatii_elevi)
    # gradinita_privata.informatii_elevi=['Bogdan', 2, '2022']

    # print(f'afiseaza :{gradinita_privata.informatii_elevi}')
    gradinita_privata.ora_de_somn()
    print(gradinita_privata.get_current_hour())
    gradinita_privata._adauga_elev(nume_elev= 'Bogdan', varsta = 3, an_inscriere='2020')
    gradinita_privata.inscriere_copil('Olimpiada de matematica', 'Bogdan')

    gradinita_privata.inscriere_copil('Olimpiada de matematica', 'Gigel Marin')
    gradinita_privata._adauga_elev(nume_elev ='Gigel Marin', varsta= 4, an_inscriere='2021')
    gradinita_privata.inscriere_copil('Olimpiada de matematica', 'Gigel Marin')

    #print(gradinita_privata.informatii_competitii)
    gradinita_privata.inscriere_copil('Olimpiada de matematica', 'David')
    #print(gradinita_privata.informatii_competitii)
    gradinita_privata.inscriere_copil('Olimpiada de biologie', 'Ionel')
    print(gradinita_privata.informatii_competitii)




