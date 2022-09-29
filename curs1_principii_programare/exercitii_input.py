input_simplu = input()

print(input_simplu)
print(type(input_simplu))

# Valoarea obtinuta prin input este MEREU str, trebuie sa facem noi type casting
varsta = input("Ce varsta ai?\n")
print(type(varsta))

varsta = int(varsta)
print(type(varsta))

# Putem face totul intr-o singura linie
anul_nasterii = int(input("In ce an te-ai nascut?"))
print(type(anul_nasterii))

# Cum preluam mai multe valori din input?
data_nasterii = input("Data nasterii (zz ll aaaa): ")
print(data_nasterii)

# Split imparte stringul in mai multe stringuri mici dupa spatii
ziua, luna, anul = data_nasterii.split()
ziua, luna, anul = int(ziua), int(luna), int(anul)
print(type(ziua), ziua)
print(type(luna), luna)
print(type(anul), anul)
