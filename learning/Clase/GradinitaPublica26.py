from learning.Clase.GradinitaPublica import GradinitaPublica
class GradinitaPublica26(GradinitaPublica):
    atribut_public ='atribut public'
    _atribut_protejat='atribut protejat'
    __atribut_privat='atribut privat'
    @property               #getter
    def atribut_privat(self):
        return self.__atribut_privat

    @atribut_privat.setter
    def atribut_privat(self, valoare):
        self.__atribut_privat = valoare

    @atribut_privat.deleter
    def atribut_privat(self):
        del self.__atribut_privat



