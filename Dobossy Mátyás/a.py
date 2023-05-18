import math

sugar = int(input("Add meg a kör sugarát: "))

kerulet = round(2 * sugar * math.pi, 2)
terulet = round(sugar * sugar * math.pi, 2)

print("A kör kerülete: ", kerulet)
print("A kör területe: ", terulet)