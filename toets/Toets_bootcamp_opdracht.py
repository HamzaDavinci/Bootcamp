# -------------------------------------------------------------------------------------------------------------------

# opdracht 1 - 
# A: het maakt de code die je maakt meer leesbaar. 
# B: dan kan je het delen met mensen en ook gelijk een backup van maken.

# -------------------------------------------------------------------------------------------------------------------

# opdracht 2:
# Maak het commentaar af.
# a = 5  # dit is een voorbeeld van het datatype: int
# b = 10.5# dit is een voorbeeld van het datatype: float
# c = "Hallo wereld" # dit is een voorbeeld van het datatype: string

# -------------------------------------------------------------------------------------------------------------------

# opdracht 3:
# Schrijf code die de waarden van a en b omwisselt. Gebruik daarvoor een extra variabele.
a = 5
b = 10
a,b = b,a
# Controleer met onderstaande code of de waarden correct zijn verwisseld
print(f"a = {a}, b = {b}") # Moet "a = 10 b = 5" printen    

# -------------------------------------------------------------------------------------------------------------------

# Opdracht 4:
# Los de problemen op (zonder exception handling).
leeftijd = int(input("Hoe oud ben je?"))
awnser = 67 - leeftijd
print(f"Dan duurt het nog ongeveer {awnser} jaar voordat je met pensioen mag!")
# Is 18 ingevuld? Dan zie je op de terminal: Dan duurt het nog ongeveer 49 jaar voordat je met pensioen mag!

# -------------------------------------------------------------------------------------------------------------------

# Opdracht 5: 
# Schrijf een functie die 3 getallen bij elkaar optelt en zorg ervoor
# dat de uitkomst ervan wordt getoond in de print
getal1 = 200
getal2 = 5
getal3 = 12
antwoord = getal1 + getal2 + getal3# of de naam van je eigen functie.
print(f"De som van {getal1} + {getal2} + {getal3} = {antwoord}")

# -------------------------------------------------------------------------------------------------------------------

# Opdracht 6:
# Maak de volgende code af:# Je moet bijbetalen als je over je minuten of je GB's heen gaat en geen onbeperkt abonnement hebt.
AANTAL_GB = 20 # Aantal GB data in je bundel
AANTAL_MINUTEN = 200 # Aantal belminuten in je bundel
ONBEPERKT = False # test ook met True
aantal_minuten_gebeld = int(input("Hoeveel minuten heb je gebeld?"))
aantal_GB_internet = int(input("Hoeveel GB's heb je gebruikt?"))
if aantal_minuten_gebeld >= AANTAL_MINUTEN or aantal_GB_internet >= AANTAL_GB and ONBEPERKT == False:
    print("Let op: je moet bijbetalen!")

else:
    print("Niet aan de hand gebruik je mobiel lekker verder!")

# -------------------------------------------------------------------------------------------------------------------

# Opdracht 7:
# Print onder elkaar de getallen 1-250 met max 2 regels code.

for nummer in range(1,251):
    print(nummer)

# -------------------------------------------------------------------------------------------------------------------

# Opdracht 8:
# Gegeven is:


# a: print een eenvoudig menu met de volgende layout:

# Onze menukaart:
# appel
# pannenkoek
# kiwi
# hamburger 
lijst_eten = ['appel', 'pannenkoek', 'kiwi', 'hamburger']

print('Onze menukaart:')
for menu in lijst_eten:
  print(menu) 

# b: Schrijf code die ervoor zorgt dat alleen het eten met de langste naam wordt geprint in de terminal. 
# Let op: je moet in de code eerst bepalen welk eten de langste naam heeft (en dus niet hardcoded 1 voor de index gebruiken). 
# test je code door extra eten toe te voegen met een nog langere naam.

HAMZA DIT MOET JE NOG DOEN

# -------------------------------------------------------------------------------------------------------------------

# Opdracht 9:
# Schrijf een programma wat de gebruiker vraagt een cijfer in te voeren via de terminal.
# Dit blijf je herhalen totdat de gebruiker een getal tussen 0 en 10 heeft ingevoerd.
# Voert de gebruiker iets anders in dan een getal: geef een foutmelding.

cijfervraag = int(input('geef me een cijfer tussen 1-10: '))
ANTWOORD_7 = 5

if cijfervraag != ANTWOORD_7:
    print ("Helaas niet goed")

else:
    print ("Goed zo, dat is het juiste antwoord!")


# -------------------------------------------------------------------------------------------------------------------

# Opdracht 10:
# repareer de volgende code:
MAX = 20
getal = print("Voer een getal in")
if getal > MAX:
   input(f"Het getal is groter dan {MAX}")
elif getal < MAX:
  input(f"Het getal is kleiner dan {MAX}")
else:
   input(f"Het getal is gelijk aan {MAX}")

# -------------------------------------------------------------------------------------------------------------------