"""
16.
Ne imaginam o echipa de fotbal pt teren sintetic.
3 Schimbari maxime admise

Declara o Lista cu 5 jucatori
Schimbari_efectuate = va jucati voi cu valori diferite
Schimbari_max = 3

Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
Efectuam schimbarea
Stergem jucatorul scos din lista
Adaugam jucatorul intrat
Afisam a intra x, a iesit y, mai aveti z schimbari
Daca jucatorul nu e in teren:
Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
Afisati ‘mai aveti z schimbari’
"""

MAX_CHANGES = 3  # constant
players = ['Adela', 'Cosmin', 'Calin', 'Mada', 'Lavinia']
changes = 0  # number of changes

# se poate face si cu for, dar acolo trebuie sa mergem pe numarul de schimbari ramase
# for i in range(MAX_CHANGES - changes):
# In cazul acesta, trebuie sa fim atenti sa nu "sarim" daca ceea ce ne da utilizatorul nu e corect

# Cat timp inca mai avem schimbari disponibile
while changes < MAX_CHANGES:
    player_out = input(f"Ce jucator vrei sa iasa de pe teren? Optiunile sunt {players}\n")
    if player_out not in players:
        print(f"nu se poate efectua schimbarea deoarece jucatorul {player_out} nu e in teren")
        print(f"Mai aveti {MAX_CHANGES - changes} schimbari")
        continue  # sare inapoi la while, practic continua sa itereze, si "sare" peste codul de mai jos

    player_in = input(f"Ce jucator vrei sa bagi in locul lui {player_out}?\n")
    players.remove(player_out)  # Stergem jucatorul scos din lista
    players.append(player_in)  # Adaugam jucatorul intrat

    changes += 1  # Incrementam numarul de schimbari efectuate, deoarece avem o schimbare valida
    print(f"A intrat {player_in}, a iesit {player_out}, mai aveti {MAX_CHANGES - changes}")

print("S-a terminat meciul!")
