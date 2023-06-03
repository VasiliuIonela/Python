lista_goala=[]
dict_gol={}

# declaram  si initializam un dict
note_elevi = {'Gigel': 10, 'Costel': 9, 'Ana': 10}
print(note_elevi)

#adaugam elemente
note_elevi['Sebi']=7
print(note_elevi)

#aflam note

print(f"Gigel are nota: {note_elevi['Gigel']}")

#actualizam valori
note_elevi['Costel']=10
print(note_elevi)
print(len(note_elevi))

#stergem valori
note_elevi.pop('Gigel')
print(note_elevi.get('Gigel', 'nu mai avem acest elev'))
print(note_elevi)
#returneaza doar cheile
print(note_elevi.keys())
