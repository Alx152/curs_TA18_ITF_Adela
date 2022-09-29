"""
Pentru toate exercitiile se va folosi notiunea de if in rezolvare.
Indirect veti exersa si operatorii in cadrul conditiilor ramurilor din if
X poate fi initializat direct in cod sau citit de la tastatura, dupa preferinte.
X este un int
"""

x = input("Introdu un numar intreg:\n")
assert x.isdigit(), f"Ati introdus {x}, care nu este un numar intreg!"
x = int(x)

"""
2. Verifica si afiseaza daca x este numar natural sau nu

=> numar natural este un numar intreg strict mai mare ca 0 
"""
if x > 0:
    print(f"{x} este numar natural")
else:
    print(f"{x} nu este numar natural")

"""
3. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
"""
if x == 0:
    print(f"{x} este neutru")
elif x > 0:
    print(f"{x} este pozitiv")
else:
    print(f"{x} este negativ")

"""
4. Verifica si afiseaza daca x este intre -2 si 13
"""
# Aici putem scrie si `-2 < x < 13`
if -2 < x and x < 13:
    print(f"{x} se afla in intervalul (-2, 13)")

"""
5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
"""
y = int(input("Introdu al doilea nr intreg:\n"))
if (x - y) < 5:
    print(f"Diferenta dintre {x} si {y} este mai mica decat 5.")


"""
6. Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)
"""
if not (5 < x < 27):
    print(f"{x}  nu este inclus in intervalul (5, 27)")

"""
7. x si y (int)
Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare
"""
if x == y:
    print(f"{x} este egal cu {y}.")
elif x < y:
    print(f"{x} este mai mic decat {y}.")
else:
    print(f"{x} este mai mare decat {y}.")

"""
8. x, y, z - laturile unui triunghi
Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
"""
z = int(input("Introdu al 3lea numar:\n"))
# Acest exercitiu se poate face in multe moduri, dar aici e foarte important cum il facem usor de citit pentru oameni!!
# Eu am ales sa plec de la echilateral, si apoi sa verific isoscel, lasand triunghiul oarecare pe ramura else (default)
if x == y == z:
    # Daca toate laturile sunt egale, putem face aceasta verificare intr-o singura instructiune
    print("Triunghi echilateral (toate laturile egale)")
elif x == y or x == z or y == z:
    # aici e suficient sa verificam daca laturile sunt egale 2 cate 2
    # nu mai e nevoie sa verificam daca cele 2 laturi sunt diferite de a 3a, deoarece daca ar fi fost asa, am fi intrat in blocul if
    print("Triunghi isoscel (2 laturi egale, una diferita)")
else:
    # daca am ajuns aici, e clar ca nici o latura nu e egala cu alta
    print("Triunghi oarecare (toate laturile diferite)")

"""
9. Citeste o litera de la tastatura
Verifica si afiseaza daca este vocala sau nu
"""
letter = input("Te rog introdu o litera:\n").lower()
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print('Litera este vocala.')
else:
    print('Litera nu este vocala.')

# Se mai poate face in alt fel, folosind `in`
# `in` verifica daca parametrul din stanga se regaseste in structura din dreapta, de exemplu daca un caracter se gaseste intr-un sir de caractere
vowels = 'aeiou'
if letter in vowels:
    print('Litera este vocala.')
else:
    print('Litera nu este vocala.')

"""
10.
Transforma si printeaza notele din sistem romanesc in  >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
"""
nota = float(input("Nota:\n"))
grade = ''
if 10 >= nota >= 9:
    grade = 'A'
elif nota >= 8:
    grade = 'B'
elif nota >= 7:
    grade = 'C'
elif nota >= 6:
    grade = 'D'
elif nota >= 4:
    grade = 'E'
elif nota >= 0:
    grade = 'F'
else:
    print("Nu ai introdus o nota valida!")

if grade:
    print(f"Nota in sistem american este {grade}")

