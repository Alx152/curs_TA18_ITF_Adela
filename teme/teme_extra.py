"""
1. Se citesc doua numere naturale de la tastatura, x si y.
Sa se afiseze toate numerele prime din intervalul [x, y], iar daca nu exista nici un
numar prim in acest interval, sa se afiseze mesajul "Nu exista numere prime in intervalul selectat [x, y]"

Exemplu:
x = 25
y = 50
Se va afisa: 29,  31, 37, 41, 43, 47

x = 25
y = 28
Se va afisa: "Nu exista numere prime in intervalul selectat [25, 28]"
"""

"""
2. Folosind stringul s declarat mai jos, sa se afiseze numarul total de vocale, respectiv numarul total de consoane.
Vocale se vor considera a, e, i, o, u. Consoane sunt toate celelalte litere (fara diacritice).
Atentie mare la spatii si semne de punctuatie, acestea nu sunt litere.
"""
s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

"""
3. Se citeste un numar natural x de la tastatura, intre 1 si 10.
Sa se afiseze in mod dinamic un pattern bazat pe numarul citit, dupa cum urmeaza:

Exemplu: x = 3
Se va afisa:
1
1 2
1 2 3

Exemplu: x = 5
Se va afisa:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

"""
4. Calatorii din autobuz:
Un autobuz merge prin oras si transporta calatori. La fiecare statie, un numar x de calatori urca, iar un numar y coboara.
Se da o lista de perechi de numere (x, y), fiecare pereche reprezinta fluxul de persoane dintr-o statie.
Sa se scrie un mic program care afisaza la fiecare statie cati calatori sunt in autobuz, iar la final sa afiseze un mesaj 
daca inca mai sunt calatori in autobuz "Inca mai sunt {z} calatori in autobuz la capat de linie. Probabil au adormit."
Se va rula pentru cele 3 exemple prezentate mai jos.
"""
statii1 = [[10,0],[3,7],[0,6]]  # la final nu vor mai fi deloc calatori
statii2 = [[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]  # la final vor mai fi 17 calatori
statii3 = [[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]  # la final vor mai fi 21 calatori adormiti

"""
5. SUPER GREU: joc x si o
Se va afisa in consola o tabla de joc x si o de 3 pe 3, iar utilizatorul va putea juca cu calculatorul.
 ___________
| 1 | 2 | 3 |
 ___________
| 4 | 5 | 6 |
 ___________
| 7 | 8 | 9 |
 ___________
 
Jucatorul va putea selecta pozitia unde pune X folosind numerele marcate pe tabla de joc.
Jucatorul si calculatorul vor pune pe rand X, respectiv O, iar tabla de joc va fi updatata cu optiunile alese dupa fiecare miscare.
Inainte de fiecare pas, se va verifica daca exista o configuratie castigatoare, iar daca da, se va opri jocul si se va afisa castigatorul.

In prima iteratie, puteti folosi randint (Google it) pentru a decide unde pune calculatorul O.
Daca vreti ceva mai greu, puteti face o strategie de castig, si sa o implementati.
"""