"""
4. Exercițiu:
- citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.
"""

my_string = input("Introdu string\n")
# Salvam primul si ultimul caracter intr-o variabila
first_char = my_string[0]
last_char = my_string[-1]
# Inlocuim primul caracter cu versiunea capitalizata peste tot, mai putin pentru primul si ultimul caracter
my_string_upper = my_string[1:-1].replace(first_char, first_char.upper())
# Stringul final va fi format din primul caracter + noul string modificat + ultimul caracter
print(first_char + my_string_upper + last_char)

"""
Versiunea 2:  in care consideram ca trebuie sa inlocuim toate caracterele, mai putin primul, si ultima daca cand apare primul.
Exemplu: cocoriccco -> coCoriCCco
0 1 2 3 4 5 6 7 8 9
c o c o r i c c c o
armasarul aramiu -> armAsArul Aramiu
"""
my_string = input("Introdu string:\n")
# Salvam primul caracter intr-o variabila (in primul exemplu c)
first_char = my_string[0]
# Salvam locatia ultimei aparitii a primului caracter intr-o variabila (in primul exemplu: 8)
first_char_last_idx = my_string.rindex(first_char)
# Salvam tot restul stringul de la ultima locatie a primului caracter (gasita anterior cu valoarea 8) pana la final
remaining_chars = my_string[first_char_last_idx:]
# Modificam restul stringului (adica intre indicii 1 - 8)
my_string_upper = my_string[1:first_char_last_idx].replace(first_char, first_char.upper())
# Afisam rezultatul final : primul caracter + stringul modificat + ce am salvat de la ultima locatie a primului caracter
print(first_char + my_string_upper + remaining_chars)