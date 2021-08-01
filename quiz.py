print('Witam w moim quizie!')
zapytanie = input('Czy chcesz zagrac? ')
if zapytanie.lower() != 'tak':
    quit()
print('Okej, zaczynajmy!')
wynik = 0
odp = input('Czy Natalia jest the best? ')
if odp.lower() == 'tak':
    print('Poprawnie')
    wynik += 1
else:
    print('Zle')
odp = input('Czy Natalia jest sufi fajowa? ')
if odp.lower() == 'tak':
    print('Poprawnie')
    wynik += 1
else:
    print('Zle')
print('To koniec!')
print('Odpowiedziales dobrze na ' + str(wynik) + ' pytania!')
print('Masz ' + str((wynik/2) * 100) + ' procent')
