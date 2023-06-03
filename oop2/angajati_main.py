from oop2.angajati import angajat
angajat1 = angajat('Ion', 'Ionescu', 'work trader')
angajat2 = angajat('Vasile', 'Mihailescu', 'tester')
angajat1.descriere()
angajat2.descriere()
angajat1.actualizare_vechime(3)
angajat2.actualizare_vechime(8)

angajat1.marire_salariu()
angajat2.marire_salariu()

angajat1.upgrade_functie('manual tester')