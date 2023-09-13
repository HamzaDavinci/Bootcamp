# opdracht 5a
startbedrag = 10000
rente_percentage = 2.8
jaar = 5
rente_jaarlijks = rente_percentage / 100 
eindbedrag_5_jaar = startbedrag * (1 + rente_jaarlijks) ** jaar

jaar = 15
eindbedrag_15_jaar = startbedrag * (1 + rente_jaarlijks) ** jaar

print(f"Na {jaar} jaar heb je {eindbedrag_5_jaar:.2f} euro.")
print(f"Na {jaar} jaar heb je {eindbedrag_15_jaar:.2f} euro.")