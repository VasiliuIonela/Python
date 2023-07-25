from learning.Clase.Gradinita import Gradinita
'''
{Bogdan: {varsta: 5, an_inscriere: 2020}}
'''
class GradinitaPrivata(Gradinita):
    __informatii_elevi = {}
    __informatii_competitii={}
    def activitate_practica(self):
        print('copiii invata sa modeleze cu plastilina')
    def ora_de_somn(self):
        print('ora de somn la gradinita privata este 3')
    @property #getter
    def informatii_elevi(self):
        return self.__informatii_elevi
    @informatii_elevi.setter
    def informatii_elevi(self, valoare):
        if isinstance(valoare, dict):
            self.__informatii_elevi= valoare
        else:
            raise Exception(f'{valoare} trebuie sa aiba tipul dict')
    @informatii_elevi.deleter
    def informatii_elevi(self):
        del self.__informatii_elevi

    def _adauga_elev(self, **kwargs):
        self.__informatii_elevi.update({kwargs['nume_elev']:
                {
                    'varsta': kwargs['varsta'],
                    'an_inscriere': kwargs['an_inscriere']
                 }
        })
        print(self.__informatii_elevi)
    def inscriere_copil(self, nume_competitie, copil):
        lista_copii=[]
        if self.__verificare_elev(copil)==True:
            try:
                lista_copii= [self.__informatii_competitii[nume_competitie]]
                lista_copii.append(copil)
                self.__informatii_competitii.update({nume_competitie: lista_copii})
            except KeyError:
                self.__informatii_competitii.update({nume_competitie: copil})
        else:
            print(f'Elevul {copil} nu este inscris la gradinita noastra')


    @property
    def informatii_competitii(self):
        return self.__informatii_competitii
    @informatii_competitii.setter
    def informatii_competitii(self, valoare):
        self.__informatii_competitii = valoare
    @informatii_competitii.deleter
    def informatii_competitii(self):
        del self.__informatii_competitii
    def __verificare_elev(self, elev):
        if elev in self.__informatii_elevi.keys():
            return True
        return False









