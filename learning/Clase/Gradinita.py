'''
Creati o clasa abstracta numita Gradinita care
sa mosteneasca clasa ABC (abstract base class)
 care sa aiba urmatoarele metode:
activitate_practica()
ora_de_somn()
Corpul primei metode va fi “pass” iar
corpul celei de-a doua metode va contine
un raise NotImplementedException
(estimeaza cineva ce inseamna acest raise NotImplementedException?).
Fiecare din cele doua metode vor avea
decoratorul @abstractbaseclass (ce este un decorator?)
'''
from abc import abstractmethod, ABC
from datetime import datetime
class Gradinita(ABC):
    @abstractmethod
    def activitate_practica(self):
        pass
    @abstractmethod
    def ora_de_somn(self):
        raise NotImplementedError('Metoda nu este implementata')
    '''
    interfata- clasa abstracta in care toate metodele sunt abstracte
    clasa abstracta - o clasa unde nu toate metodele sunt abstracte
    
    '''
    @classmethod
    def get_current_hour(self):
        return datetime.now()
