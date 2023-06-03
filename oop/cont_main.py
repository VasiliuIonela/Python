from oop.cont_bancar import ContBancar

cont1 = ContBancar('Ionela', 'RO001')
cont2 = ContBancar('David', 'RO002')
cont1.activare_cont(7777)
cont2.activare_cont(3333)
cont2.activare_cont(4444)
cont2.activare_cont(7777)

cont1.alimentare_cont(300)
cont2.alimentare_cont(700)

cont1.interogare_sold()


