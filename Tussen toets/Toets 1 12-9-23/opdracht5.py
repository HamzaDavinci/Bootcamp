from time import sleep # je hoeft nog niet te weten wat een import is, Kopieer deze regel en je kunt je programma laten wachten met de opdracht sleep(x seconden)


oppervlakte = int(input('Hoeveel m2 vloerbedekking heeft u nodig?'))
prijs_m2 = 40


geduld = 5 * ("Een moment geduld a.u.b., de scherpste prijs wordt berekend." ,"Een moment geduld a.u.b., de scherpste prijs wordt berekend.")

for x in geduld:
  print(x)
    
# secret code containing the answer of question 4

# end of secret

totaal = prijs_m2 * oppervlakte

print(f'Het scherpste prijs voor een oppervlakte van {oppervlakte} m2 is: Eur ' + str(totaal))
