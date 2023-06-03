class ContBancar:
    # constructor
    def __init__(self, titular_cont, iban):
        self.titular_cont = titular_cont
        self.iban = iban
        self.sold = 0
        self.activ = False
        self.pin = 7777
        self.incercari_activare = 0

    def interogare_sold(self):
        print(f'Titular cont {self.titular_cont}')
        print(f'iban {self.iban}')
        print(f'sold {self.sold}')
        print(f'Activ {self.activ}')
        print(f'incercari {self.incercari_activare}')
        print('-------')

    def activare_cont(self, pin_utilizator):
        self.salut()
        if pin_utilizator == self.pin:
            print('Card activat')
            self.activ = True
        else:
            print('Pin gresit')
            self.incercari_activare += 1

    def alimentare_cont(self, suma_depusa):
        self.salut()
        self.sold += suma_depusa
        print(f'Ati depus cu succes suma de {suma_depusa} Aveti in cont {self.sold}')

    def plata_card(self, suma_cheltuita):
        self.salut()
        if suma_cheltuita <= self.sold:
            self.sold -= suma_cheltuita
            print(f'Ai cheltuit: {suma_cheltuita}')
            print('Mai ai: self.sold')
        else:
            print('Fonduri insuficiente')

    def salut(self):
        print(f'Buna, {self.titular_cont}')
