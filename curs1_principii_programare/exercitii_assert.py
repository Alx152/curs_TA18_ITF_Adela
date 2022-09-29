a = 1

# Daca valoarea lui a este inca 1, codul merge mai departe; daca nu, da eroaare
assert a == 1
print("Codul merge mai departe")

# # Aici va da eroare
# assert a == 5
# print("Codul merge mai departe")


# Exemplu: facem testare pe un site de vanzare de bilete online, iar contorul biletelor trebuie sa fie mereu pozitiv
nr_bilete = 100
assert nr_bilete >= 0

# # Assert poate afisa si un mesaj atunci cand da eroare
# nr_bilete = -1
# assert nr_bilete >= 0, f"Numarul de bilete este MAI MIC ca 0 (este {nr_bilete})"


# Exemplu 2: verficam daca un student are medie de trecere la examene
nota1, nota2, nota3, nota4 = 5, 7, 3, 7
media = (nota1 + nota2 + nota3 + nota4) / 4
assert media >= 5.0

# # Daca la examenul 2 ar fi luat nota mai mica, nu mai trecea
# nota2 = 4
# media = (nota1 + nota2 + nota3 + nota4) / 4
# assert media >= 5.0, f"Ne vedem in toamna la restante!"


# Exemplu 3: putem folosi assert si ca sa ne asiguram ca tipurile si valorile de date asteptate sunt cele dorite
nr_intreg = input("Introdu un numar intreg intre 1 si 99")
assert nr_intreg.isdigit(), f"{nr_intreg} NU este un numar intreg!"
assert 1 <= int(nr_intreg) <= 99, f"{nr_intreg} NU este cuprins in intervalul 1 - 99"
