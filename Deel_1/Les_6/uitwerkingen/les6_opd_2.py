# opdracht 2a

a = int(input("Voer de waarde van a in: "))
b = int(input("Voer de waarde van b in: "))

if a > b:
    print(f"Variabele a is het grootst want {a} is groter dan {b}")
elif b > a:
    print(f"Variabele b is het grootst want {b} is groter dan {a}")
else:
    print("Variabele a en b zijn gelijk.")
