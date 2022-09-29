# Numele pentru variabile pot contine litere mari, mici, cifre, si caracterul underscore (_)
my_var = 5
# Aceasta este o var acceptata de compilator, dar nu respecta standardul snake_case din Python
myVar = 100
user1 = 'Ion Popescu'
# Var trebuie sa inceapa cu litera sau _, niciodata cu cifre
# 1user = 'Maria Popescu'

# daca vrem sa incepem un nume de variabila cu litera mare, trebuie tinut cont de faptul ca standardul este ca acestea sa fie constante
DAYS_IN_WEEK = 7  # numim asta constanta
# DAYS_IN_WEEK = 100
#
# print(DAYS_IN_WEEK)

# Pot pune _ la inceputul unei variabile, dar momentan nu va recomand
_var = 100

# Aceste variabile sunt diferite, deoarece python este case-sensitive
myvar = 5
myVar = 7

# Asignare multipla
a, b, c = 10, 20, 30
# O sa dea eroare, numarul de variabile si numarul de valori nu coincid
# d, e, f = 1, 2, 3, 4

# Putem asigna aceeasi valoare mai multor variabile
g = h = i = 'Sir de caractere'

var1 = 2000 + 3000
var2 = 5000

print(var1 is var2)  # False
print(var1 == var2)  # True

# Initializare string gol
user_input = ""

# Numele de variabile NU POT FI KEYWORDS
# class = 10
# https://www.programiz.com/python-programming/keywords-identifier#:~:text=Keywords%20are%20the%20reserved%20words,structure%20of%20the%20Python%20language.

# Numele de variabile NU e recomandat sa fie nici alt cuvant folosit in general in python (nume de functii, etc)
print = 100
# print(print)  # Aici o sa dea eroare, pentru ca noi am suprascris functia print, facand-o integer

# Numele trebuie sa fie explicite
alfa = 'BMW seria 7'  # BAD
marca_masina = 'Jeep Compass'  # GOOD
