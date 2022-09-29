"""
Clasa Patrat
"""

class Patrat:

    def __init__(self, latura, culoare):
        self.latura = latura
        self.culoare = culoare

    def aria(self):
        return self.latura ** 2

    def perimetru(self):
        return self.latura * 4

    def schimba_culoarea(self, culoare_noua):
        print(f"Culoarea originala este {self.culoare}, o schimbam cu {culoare_noua}")
        self.culoare = culoare_noua


patrat_rosu = Patrat(5, "rosu")
patrat_verde = Patrat(7, "verde")

print(f"Patratul rosu are aria {patrat_rosu.aria()}")
print(f"Patratul verde are perimetrul {patrat_verde.perimetru()}")

print(patrat_rosu.culoare)
patrat_rosu.schimba_culoarea("galben")
print(patrat_rosu.culoare)
