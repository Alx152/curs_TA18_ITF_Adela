"""
11.Verifica daca x are minim 4 cifre (x e int)
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
"""
x = 5435
if x > 999:
    print("Minim 4 cifre")

"""
12.
Verifica daca x are exact 6 cifre 
"""
x = 543534
if 10**6 <= x < 10**7:  # putem folosi puterile lui 10, ca sa nu ne complicam cu numaratul cifrelor
    print("Nr are exact 6 cifre")
else:
    print("Nr nu are exact 6 cifre")

"""
13.
Verifica daca x este numar par sau impar (x e int)
"""
if x % 2 == 0:
    print("Este nr par")
else:
    print("Este nr impar")

"""
14.
x, y, z (int)
Afiseaza care este cel mai mare dintre ele?
"""
x, y, z = 3, 7, 1
if x > y:
    if x > z:
        print(f"{x} este cel mai mare")
    else:
        print(f"{z} este cel mai mare")
else:
    if y > z:
        print(f"{y} este cel mai mare")
    else:
        print(f"{z} este cel mai mare")

"""
15. 
X, y, z - reprezinta unghiurile unui triunghi
Verifica si afiseaza daca triunghiul este valid sau nu
"""
# Un triunghi este valid daca toate unghiurile sunt strict mai mari ca 0, iar suma lor este 180 grade
if (x > 0 and y > 0 and z > 0) and (x + y + z == 180):
    print("Triunghi valid")

"""
16. 
Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
cititi de la tastatura un int x
afiseaza stringul fara ultimele x caractere
ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
"""
x = 7
my_string = "Coral is either the stupidest animal or the smartest rock"
print(my_string[0:len(my_string) - x])
print(my_string[:-x])  # Echivalent cu ce avem mai sus, Python infereaza inceputul stringului, iar la final putem folosi indexarea negativa

"""
17.
acelasi string
declara un string nou care sa fie format din primele 5 caractere + ultimele 5
"""
new_string = my_string[0:5] + my_string[-5:]

"""
18.
acelasi string
salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
(hint: este o functie care te ajuta sa faci asta)
folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
output: 'Coral is either the stupidest animal or the smartest ' 
"""
# Putem gasi indexul cu find sau cu index (ambele vor returna prima aparitie a cuvantului rock)
rock_index = my_string.index('rock')
# rock_index = my_string.find('rock')
print(my_string[0:rock_index])

"""
19. 
citeste de la tastatura un string
verifica daca primul si ultimul caracter sunt la fel
se va folosi un assert
atentie: se doreste ca programul sa fie case insensitive
'apA' e acceptat
"""
s = "apA"
# Putem compara cu upper sau lower, nu conteaza, cat timp in ambele parti folosim aceeasi functie
assert s[0].upper() == s[-1].upper()  # comparam A si A
assert s[0].lower() == s[-1].lower()  # comparam a si a

"""
20. 
avand stringul '0123456789'
afisati doar numerele pare 
acum afisati doar numerele impare
(hint: folositi slicing, controlati din pas
"""
# Il consideram pe 0 ca fiind par
digits = "0123456789"
even = digits[ : :2]  # echivalent cu digits[0:len(digits):2]
odd = digits[1:len(digits):2]
