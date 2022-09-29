"""
Metode polimorfice (forme multiple) - au acelasi nume, dar actioneaza diferit.
"""

"""
Zicem ca metoda len este polimorfica, deoarece are multiple implementari (pentru lista, pentru string, pentru dictionar),
DAR toate aceste implementari se apeleaza la fel.
"""
l = [1, 2, 3]
print(len(l))
s = "12344nkfsd"
print(len(s))
d = {1: "a", 2: "b", 3: "c"}
print(len(d))
