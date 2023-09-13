# opdracht 3a

leeftijd = int(input('Wat is uw leeftijd? '))
snor = input('Heeft u een snor? ').lower()

diploma = 'U heeft de baan behaald'
geen_diploma = 'U heeft de baan niet behaald'
baan = 'U krijgt de baan'

print(diploma if leeftijd >= 18 else geen_diploma)
print(baan if leeftijd >= 18 or snor == 'ja' else 'U krijgt de baan niet')



