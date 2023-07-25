# tema: definiti o functie draw in clasa copil care sa suprascrie complet functia draw
# din clasa parinte
#cum trebuie modificata fct din cls Patrat_b pt a a obt acest rezultat?
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
class Patrat_b(Poligon):
    def __init__(self, culoare):
        super().__init__(4, "Patrat", culoare)

    def draw(self, lungime_latura):
        print(f'Vreau sa desenez un patrat cu lungimea laturilor de: {lungime_latura} cm')
        perimetru = 4 * lungime_latura
        print(f'Perimetrul patratului este: {perimetru} cm')

patrat = Patrat_b('red')
patrat.draw(5)
