#crearea unei clase
# class Dreptunghi:
#     latime =100
#     lungime=200
# class Dreptunghi:
#     def __init__(self, latime, lungime): #ca la orice functie, putem folosi valori prestabilite care vor putea fi suprascrise
#         self.latime = latime
#         self.lungime = lungime
#     def calculeaza_aria(self):
#         return self.latime*self.lungime
#     def calculeaza_perimetrul(self):
#         return 2*(self.latime + self.lungime)
#
# dreptunghi = Dreptunghi(100,200)
# print(type(dreptunghi))
# print(f'Aria: {dreptunghi.calculeaza_aria()}')
# print(f'Permetrul :{dreptunghi.calculeaza_perimetrul()}')
import turtle


# class Pisica:
#     def __init__(self, nume, rasa, varsta):
#         self.nume = nume
#         self.rasa = rasa
#         self.varsta = varsta
#     def comunica(self):
#         print(f'Pisica {self.nume} face Miau miau')
#     def se_joaca(self, jucarie):
#         print(f'Pisica {self.nume} se joaca cu {jucarie}')
# pisica =Pisica('Pisi', 'siameza', 1)
# pisica.comunica()
# pisica.se_joaca('ghem')

# class Catel:
#     def __init__(self, nume, rasa, varsta, stare):
#         self.nume = nume
#         self.rasa = rasa
#         self.varsta = varsta
#         self.stare = stare
#     def latra(self):
#         print(f'cainele {self.nume} face ham ham. ')
#     def se_joaca(self, jucarie):
#         if self.stare =='happy':
#             print(f'Cainele {self.nume} se joaca cu {jucarie}.')
#         else:
#             print(f'Cainele {self.nume} nu are chef de joaca.')
# catel = Catel('Cutu', 'maidanez', 3, 'happy')
# catel2= Catel('Jack', 'cocker', 2, 'marait')
# catel.latra()
# catel.se_joaca('os')
# catel2.se_joaca('mingea')
import turtle
class Poligon:
    def __init__(self, laturi, nume, culoare):
        self.laturi = laturi
        self.__nume = nume
        self.culoare = culoare
        self.total_unghiuri= (self.laturi -2)*180
        self.unghi = self.total_unghiuri/self.laturi
    def actualizeaza_nume(self, nume):
        self.__nume = nume
    def afiseaza_nume(self):
        return self.__nume
    def deseneaza(self):
        for i in range(self.laturi):
            turtle.forward(100)
            turtle.left(180-self.unghi)
            turtle.color(self.culoare)
            #turtle.left(90) # valoarea unghiurilor unui patrat in grade
        turtle.done() # valoarea totala a unghiurilor unui poligon (n-2)*180


patrat= Poligon(4, 'Patrat', 'albastru')
print(patrat.afiseaza_nume(),patrat.culoare)
#patrat.nume='triunghi'
# patrat.actualizeaza_nume('triunghi')
# print(patrat.afiseaza_nume(), patrat.culoare)
#patrat.deseneaza()
triunghi = Poligon(3, 'Triunghi', 'red')
triunghi.deseneaza()

#deseneaza triunghi, hexagon