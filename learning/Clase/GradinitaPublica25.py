from learning.Clase.GradinitaPublica import GradinitaPublica
from learning.Clase.Prst import Prst
class GradinitaPublica25(GradinitaPublica):
    def activitate_practica(self):
        print('Copiii se joaca in curte pe balansoar')
    '''
    In interiorul clasei GradinitaPublica25 creati o noua 
    metoda care sa primeasca de la tastatura numarul de 
    buline rosii pe care le-a primit fiecare elev in parte, 
    procesati-le si calculati media aritmetica a numarului de buline rosii. 
    Daca aceasta este mai mare decat cinci, printati pe ecran: 
    “Elevii acestei gradinite sunt foarte neastamparati”.
    '''
    def calculam_buline(self):
        nr_elevi =int(input('Cati elevi sunt in gradinita?\n'))
        suma_buline =0
        for elev in range(1,nr_elevi+1):
            nr_buline=int(input(f'Introduceti nr de buline rosii pentru elevul {elev}: '))
            suma_buline+= nr_buline
        media_buline_elevi = suma_buline/nr_elevi
        print(f'Media bulinelor elevilor este: {media_buline_elevi}')
        if media_buline_elevi> 5:
            print(f'{Prst.RED}Elevii acestei gradinite sunt foarte neastamparati{Prst.RESET}')

    '''
    In interiorul clasei GradinitaPublica25 creati o noua metoda 
    care sa primeasca de la tastatura un dictionar care sa contina o serie 
    de perechi cheie:valoare si dictionare imbricate (embedded, nested) care 
    sa contina urmatoarele informatii: numele elevului, numele parintilor, 
    varsta elevului, activitatea preferata. 
    Printati pentru fiecare elev toate informatiile de mai sus.
    {'elev1':{'nume' : 'Andrei', 'nume_parinti': 'Elena si Adi Popescu', 'varsta': 5, 'activitate_preferata' : 'desen'}, 'elev2':{'nume' : 'Ema', 'nume_parinti': 'Ioana si Vasile Crisan', 'varsta': 4,'activitate_preferata' : 'dans'}}
    '''

    def introduceti_informatii_elevi(self):
        info= eval(input('Introduceti datele despre elevi\n'))
        for elev, detalii in info.items():
            print(f'elevul {elev}: ')
            for date, valoare in detalii.items():
                print(f'{date}: {valoare}')

