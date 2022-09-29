# user = parametru pentru functia hello_user
# putem apela functia cu diferite valori ale acestui parametru
def hello_user(user):
    print(f"Hello, {user}")
    print("Have a nice day!\n")


# hello_user("Adela")
# hello_user("Lavinia")
# hello_user("Cosmin")

def add_two(a, b):
    print(f"Primul numar este {a}")
    print(f"Al doilea numar este {b}")
    print(f"Suma celor 2 numere este {a+b}\n")

# Parametri pozitionali (a devine 1 pentru ca e primul, b devine 7)
add_two(1, 7)
# Parametri numiti (named parameters):
# pasam valorile functiei bazat pe numele pe care le-am folosit la definire
add_two(b=1, a=7)
# add_two(-5, 13)
# add_two(0, 0)
# add_two(3.14, 1.71)

# a = int(input("Scrie a:\n"))
# b = int(input("Scrie b:\n"))
# add_two(a, b)

# Parametrii pot avea valori implicite, adica nu este necesar sa le mai dam noi o valoare
# atunci cand apelam functia (sunt parametri optionali)
# user - parametru obligatoriu!!
# msg - parametru optional
def hello_user_custom(user, msg="Have a nice day!"):
    print(f"Hello, {user}")
    print(f"{msg}\n")
    x = 100
    print(x)

# hello_user_custom()  # va da eroare, deoarece nu avem valoare pentru parametrul obligatoriu "user"
hello_user_custom("Adela")
hello_user_custom("Adela", "Good morning!")

# Parametri functiilor nu exista DECAT in corpul functiei in care sunt definiti
# print(msg)  # eroare

# La fel si pentru orice variabile definite in interiorul unei functii,
# aceasta nu exista in afara functiei in care a fost declarata
# print(x)  # eroare