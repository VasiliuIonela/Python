class angajat:
    #constructor
    def __init__(self, nume):
        self.nume = nume
        self.prenume = prenume
        self.vechime = vechime
        self.functie = functie
        self.salariu = salariu

    def descriere(self):
        print(f'Numele si prenumele angajatului este: {self.nume} {self.prenume}')
        print(f'Functia acestui angajat este de {self.functie}')
        print(f'{self.nume} {self.prenume} are o vechime de {self.vechime} ani')
        print(f'Salariul acestuia este de {self.salariu}')

    def actualizare_vechime(self, noua_vechime):
        self.vechime = noua_vechime

    def marire_salariu(self):
        if self.vechime <=5:
            self_salariu += 300
        if self.vechime > 5:
            self.salariu +=500




