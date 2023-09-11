naam = input('Hallo wat is jouw naam? ')
leeftijd = int(input('Hallo wat jouw leeftijd? '))

if leeftijd < 18:
    print (f'Beste {naam}, je bent nog geen 18. Alleen autorijden zit er dus niet in :-( ')

if leeftijd > 18:
    print (f'Beste {naam}, je bent 18 of ouder en mag dus alleen autorijden (met rijbewijs althans).')