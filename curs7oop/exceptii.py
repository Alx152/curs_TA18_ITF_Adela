# """
# Exceptii: mecanism try-except
# """
#
# l = [1, 2, 3, 4]
# try:
#     print(l[6])
# except IndexError as e:
#     print(f"A aparut o eroare: {e.args}")
#
# print(l[1])
#
# """
# Exemplu unde as putea folosi try-except
#
# Astept un anumit tip de input de la utilizator
# """
# try:
#     varsta = int(input("Introduceti varsta:\n"))
# except ValueError as e:
#     print("Nu ati introdus un numar, ci altceva!")
#
# print("Am terminat programul!")


"""
Exemplu cu assert
Putem avea blocuri except multiple, dar sunt cateva reguli:
1. Trebuie mereu sa mergem de la exceptia cea mai specifica, la cea mai generica.
2. Putem avea si un bloc de except simplu (fara sa specificam o clasa de exceptie), dar nu e recomandat.
"""
try:
    x = int(input("Introduceti un numar par:\n"))
    assert x % 2 == 0
except ValueError as e:
    print(f"Nu ati introdus un numar, ci altceva")
except AssertionError as e:
    print(f"Nu ati introdus un numar par: {e.args}")
except:
    print("A aparut o alta exceptie, nu cele la care ma asteptam eu")

print(f"Numarul introdus este {x}")
