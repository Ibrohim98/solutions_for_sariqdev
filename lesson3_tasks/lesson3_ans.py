#lesson 3 answers for questions
# Q1 5 ning 4-darajasini toping
from math import sqrt

print("the fourth power of five is:", 5 ** 4)

# Q2 22 ni 4 ga bo'lganda qancha qoldiq qoladi?
print("22 ni 4 ga bo'lganda qoldiq:", 22 % 4)

# Q3 Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping
a = 125
Area = a ** 2
Perimet_of_square = 4 * a
print(f"Area: {Area},\nPertimetr: {Perimet_of_square}")

# Q4 Diametri 12 ga teng bo'lgan doiraning yuzini toping  ( π=3.14 deb oling)
pi = 3.14
diametr = 12
radius = diametr / 2
area_of_round = pi * (radius ** 2)
print(f"Aylananing yuzasi: {area_of_round}")

# Q5 Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping
# (Pifagor teoremasidan foydalaning)
a_katet = 6
b_katet = 7
c_gipotenuza = sqrt(a_katet ** 2 + b_katet ** 2)
print(f"Gipotenuza uzunligi {c_gipotenuza}")
