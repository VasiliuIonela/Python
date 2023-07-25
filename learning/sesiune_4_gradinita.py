# from abc import abstractmethod, ABC
#
# class Gradinita(ABC):
#     @abstractmethod
#     def joaca(self):
#         raise NotImplementedError # am instruit sistemul sa returneze o eroare specifica daca metoda nu este implementata
#     def somn(self):
#         print('copiii dorm')
#     @abstractmethod
#     def activitati(self):
#         pass
#
# class Gradinita_privata(Gradinita):
#     nr_copii = 0
#     adresa = None
#     orar = None
#     def joaca(self):
#         print("copiii alearga")
#
#     def activitati(self):
#         print("Copiii coloreaza")
# class Gradinita_publica(Gradinita):
#     nr_copii = 0
#     adresa = None
#     orar = None
#     def joaca(self):
#         #super().joaca()  - apelarea fct joaca din clasa parinte, care, fiind abstracta, returneaza o eroare
#         print("copiii sar coarda")
#     def activitati(self):
#         print("copiii canta")
#
# gradinita_publica1 = Gradinita_publica()
# gradinita_publica1.joaca()
# gradinita_publica1.activitati()
# gradinita_publica1.somn()

# import turtle
#
class Poligon():
    def __init__(self, laturi, nume, culoare):
        self.laturi = laturi
        self.nume = nume
        self.culoare = culoare
    def draw(self):
        turtle.color(self.culoare)
        for i in range(self.laturi):
            turtle.forward(100)
            turtle.right(90)
        turtle.done()
#
#
# class Patrat(Poligon):
#     def __init__(self, culoare):
#         super(Patrat, self).__init__(4, "Patrat", culoare)
#
# patrat = Patrat('blue')
# patrat.draw()
class Patrat_b(Poligon):
    def __init__(self, culoare):
        super().__init__(4, "Patrat", culoare)
    def draw(self,lungime_latura):
        print(f'Vreau sa desenez un patrat cu lungimea laturilor de: {lungime_latura} cm')
        perimetru= 4*lungime_latura
        print(f'Perimetrul patratului este: {perimetru} cm')

patrat =Patrat_b('red')
patrat.draw(3)
# tema: definiti o fct draw in clasa copil care sa suprascrie complet fct draw din clasa parinte
#cum trebuie modificata fct din cls Patrat_b pt a a obt acest rezultat

# class A():
#     pass
# class B():
#     pass
#
# class C(A,B, str):
#     nume = 'C'
#     def care_este_mostenirea(self):
#         return issubclass(C,str) # C, A-true, C,B-true, C,object(cls predefinita)-true
# clasa_c= C()
# print(clasa_c.care_este_mostenirea())
