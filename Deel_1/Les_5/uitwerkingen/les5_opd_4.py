# opdracht 4a

straal = 5
pi = 3.14159

oppervlakte = straal * straal * pi
omtrek = 2 * pi * straal

print(f"De oppervlakte van een cirkel met straal {straal} is {oppervlakte}")
print(f"De omtrek van een cirkel met straal {straal} is {omtrek}")

gebruiker_straal = float(input("Voer de straal van de cirkel in: "))

oppervlakte_gebruiker = gebruiker_straal * gebruiker_straal * pi

omtrek_gebruiker = 2 * pi * gebruiker_straal

print(f"De oppervlakte van een cirkel met straal {gebruiker_straal} is {oppervlakte_gebruiker}")
print(f"De omtrek van een cirkel met straal {gebruiker_straal} is {omtrek_gebruiker}")
