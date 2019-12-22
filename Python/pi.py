from decimal import Decimal
summe = int(1)
for i in range(2, 2000):
    zahl = Decimal(1/(i**4))
    summe += zahl
    
summe *= 90
summe **= Decimal(0.5)
summe **= Decimal(0.5)
print(Decimal(summe))
