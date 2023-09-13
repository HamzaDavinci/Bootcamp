# opdracht 9a

collegegeld_per_student = 2000
aantal_studenten = 50

totaal_collegegeld = collegegeld_per_student * aantal_studenten

prijs_appels = 3.40
prijs_druiven = 2.45
prijs_bananen = 1.95

btw_tarief = 0.09

btw_appels = btw_tarief * prijs_appels
btw_druiven = btw_tarief * prijs_druiven
btw_bananen = btw_tarief * prijs_bananen

totaal_btw = btw_appels + btw_druiven + btw_bananen

print(f"Totaal collegegeld betaald door alle studenten: €{totaal_collegegeld}")
print(f"Totaal BTW op fruit: €{totaal_btw}")
