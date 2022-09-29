# Set = o structura de date asemanatoare listei, care NU permite elemente duplicate si NU este ordonat sau indexat
s = {1, 2, 3, 3}
l = [1, 2, 3, 3]
print(s)  # va printa {1, 2, 3}, deoarece va sterge automat un 3

print(l[1])
# print(s[1])  # Va da eroare
# s = {}  # Cu acolade goale facem un DICTIONAR
set_empty = set()  # CA sa initializam un set gol, folosim chiar functia set
set_from_list = set(["alfa", 1, True, 5, 5])
print(set_from_list)

# Exemplu: Verificare daca lista are doar elemente unice: o transformam in set, si verificam lungimea
lst = ["alfa", 1, True, 5, 5]
if len(lst) == len(set(lst)):
    print("Lista are doar elemente unice")
else:
    print("Lista NU are doar elemente unice")

# Nu putem modifica elemente existente in set, deoarece nu avem cum sa le accesam
# In schimb, putem sterge si putem adauga
print(s)
s.add(5)
s.add(3)
print(s)
s.remove(3)
# s.remove(4)  # o sa dea eroare daca nu exista
if 4 in s:  # set membership: verificam daca valoarea este in set inainte sa dam remove
    s.remove(4)
print(s)
print(f"Setul are lungimea {len(s)}")