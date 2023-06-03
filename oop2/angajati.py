class angajat:
    #constructor
    def __init__(self, nume, prenume, functie):
        self.nume = nume
        self.prenume = prenume
        self.vechime =0
        self.functie =functie
        self.salariu =3000

    def descriere(self):
        print(f'Numele si prenumele angajatului este: {self.nume} {self.prenume}')
        print(f'Functia acestui angajat este de {self.functie}')
        print(f'{self.nume} {self.prenume} are o vechime de {self.vechime} ani')
        print(f'Salariul acestuia este de {self.salariu}')
        print('-----------------------------')

    def actualizare_vechime(self, noua_vechime):
        self.vechime = noua_vechime
        print(f'Vechimea  noua este: {self.vechime}')

    def marire_salariu(self):
        if self.vechime <=5:
            self.salariu += 300
        if self.vechime > 5:
            self.salariu +=500
        print(f'Noul salariu este de {self.salariu}')

    def upgrade_functie(self, functie):
        self.functie = functie
        print(f'Noua functie pentru acest angajat este: {self.functie}')




