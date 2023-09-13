# opdracht 5a

a = int(input("Voer de waarde van a in: "))
b = int(input("Voer de waarde van b in: "))
c = int(input("Voer de waarde van c in: "))

if a > b and a > c:
    print(f"Variabele a is het grootst, want {a} is groter dan {b} en {c}.")
elif b > a and b > c:
    print(f"Variabele b is het grootst, want {b} is groter dan {a} en {c}.")
elif c > a and c > b:
    print(f"Variabele c is het grootst, want {c} is groter dan {a} en {b}.")
else:
    print("De variabelen a, b en c zijn gelijk.")
