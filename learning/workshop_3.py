#Creati o clasa cinema in care sa stocati atributele si metodele de care e nevoie ca sa puteti sa gestiona
# un sistem de tip cinema (acestea vor fi implementate la alegerea voastra). Clasa nu va avea constructor.
# Creati cel putin 5 metode de test si 10 atribute.

class Cinema:
    filme = ['Titanic', 'Avengers', 'Superman']
    an_aparitie = [1990, 2002, 2010]
    nr_locuri = 200
    program_film =[16, 18, 20]
    tipologie_film =('2D', '3D', '4DX')
    gen_film = ('actiune', 'aventura', 'horror', 'SF')
    locatie = 'Iulius Mall'
    pret_bilet = 30
    durata_film = 120
    sali =['Sala1','Sala2','Sala3']
    nr_bilete_vandute = 0
    def adauga_film(self, nume_film):
        lista_filme = self.filme.copy()
        lista_filme.append(nume_film)
        self.filme = lista_filme
    def discount_pret(self, discount):
        return self.pret_bilet-self.pret_bilet*discount/100
    def descriere_cinema(self):
        print(f'Filme: {self.filme}')
        print(f'anul aparitiei: {self.an_aparitie}')
        print(f'Locatie cinema: {self.locatie}')
        print(f'Pret bilet: {self.pret_bilet}')
        print(f'Durata filmului: {self.durata_film}')
        print(f'Numar locuri sala: {self.nr_locuri}')
    def cumpara_bilet(self, nr_bilete):
        self.nr_locuri -=nr_bilete
        self.nr_bilete_vandute +=nr_bilete
    def incasari_cinema(self):
        return self.pret_bilet*self.nr_bilete_vandute

cinema_city=Cinema()
# cinema_city.descriere_cinema()
# cinema_city.cumpara_bilet(5)
# cinema_city.descriere_cinema()
# print(f'incasari: {cinema_city.incasari_cinema()} lei')
cinema_city2 = Cinema()
cinema_city3= Cinema()
cinema_city2.locatie= 'vivo Cluj Napoca'
cinema_city3.locatie='Mall Bucuresti'
cinema_city2.adauga_film('Venom')
cinema_city3.adauga_film('Flash')
#Apelati pe rand fiecare dintre metodele create si respectiv printati  pe ecran toate valorile atributelor pentru fiecare obiect.
# Printarea se va face cu formatare si, pentru o complexitate mai mare, puteti sa puneti toate obiectele instantiate
# intr-o lista pe care sa o parcurgeti cu un for (si astfel sa faceti printarea pentru toate elementele concomitent).
# Repetati actiunea cu while si respectiv cu foreach. Rulati codul.
lista_cinema = [cinema_city,cinema_city2, cinema_city3]

# for index_cinema in range(len(lista_cinema)):
#     print('#'*25)
#     lista_cinema[index_cinema].descriere_cinema()
#     print(f'tipologie filme: {lista_cinema[index_cinema].tipologie_film}')
#     print(f'gen film: {lista_cinema[index_cinema].gen_film}')
#     print(f'sali cinema: {lista_cinema[index_cinema].sali}')

# index_cinema=0
# while index_cinema < len(lista_cinema):
#     print('#' * 25)
#     lista_cinema[index_cinema].descriere_cinema()
#     print(f'tipologie filme: {lista_cinema[index_cinema].tipologie_film}')
#     print(f'gen film: {lista_cinema[index_cinema].gen_film}')
#     print(f'sali cinema: {lista_cinema[index_cinema].sali}')
#     index_cinema+=1

for cinema in lista_cinema:
    print('#' * 25)
    cinema.descriere_cinema()
    print(f'tipologie filme: {cinema.tipologie_film}')
    print(f'gen film: {cinema.gen_film}')
    print(f'sali cinema: {cinema.sali}')









