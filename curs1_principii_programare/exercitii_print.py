# Concatenare de stringuri
str1 = "mere"
str2 = "pere"
print("Mie imi place sa mananc " + str1 + " si " + str2)

# Nu putem concatena int/float/bool si string
var_int = 15
# print(str1 + var_int)  # o sa dea eroare, nu putem concatena str si int
print(str1 + str(var_int))

# Formatare de stringuri
n1 = 10
n2 = 5
print(f"Mie imi place sa mananc {n1} {str1} si {n2} {str2}")
# Intre acolade se pot pune instructiuni Python, nu doar variabile
print(f"Mie imi place sa mananc {n1 + 5} {str1} si {n2} {str2}")

# Se pot printa mai multe variabile, cu virgula intre ele (separatorul va fi spatiu)
print(str1, str2, n1, n2)
print(str1, str2, n1, n2, end=' +++ ')
print(str1, str2, n1, n2, sep=' | ')
