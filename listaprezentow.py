
from os import system
from sys import exit
from random import shuffle

lista_imion = []

while True:
    system('cls')
    if len(lista_imion) > 0:
        print('Obecnie na liście znajduje się: ')
        for imie in lista_imion:
            print(chr(100003), imie)
    czy_dodac = input('Czy chcesz dodać imię do listy? (t/n): ').strip().lower()
    
    if czy_dodac == 't':
        do_dodania = str.capitalize(str.strip(input('Podaj imię: ')))
        if do_dodania in lista_imion:
            print('Podane imię już znajduje się na liście. Podaj wartość unikatową:')
        elif len(do_dodania) == 0:
            print('Należy podać imię.')
        else:
            lista_imion.append(do_dodania)
            print('Dodano imię do listy.')
        input('Naciśnij Enter, aby kontynuować.')
    elif czy_dodac == 'n':
        if len(lista_imion) < 3:
            while True:
                print('Lista jest za krótka.')
                czy_zakonczyc = input('Czy chhcesz zakończyć działanie programu (t/n): ')
                
                if czy_zakonczyc == 't':
                    exit(0)
                elif czy_zakonczyc == 'n':
                    break
                else:
                    system('cls')
                    print('Podano nieprawidłową odpowiedź.')
        else:
            break
    else:
        print('Podano nieprawidłową odpowiedź.')
        input('Naciśnij Enter, aby kontynuować.')
        
shuffle(lista_imion)

mikolaj = {}

for i in range(len(lista_imion)):
    if i != len(lista_imion) -1:
        mikolaj[lista_imion[i]] = lista_imion[i + 1]
    else:
        mikolaj[lista_imion[i]] = lista_imion[0]
        
lista_do_wyswietlenia = list(mikolaj.items())

shuffle(lista_do_wyswietlenia)

for i in range(len(lista_do_wyswietlenia)):
    system('cls')
    input('Naciśnij Enter, aby kontynuować.')
    system('cls')
    print('Teraz losować będzie', lista_do_wyswietlenia[i][0])
    input('Naciśnij Enter, aby kontynuować. Upewnij się, że są osoby nielosujące nie patrzą.')
    system('cls')
    print(lista_do_wyswietlenia[i][0], 'kupujesz prezent dla', lista_do_wyswietlenia[i][1])
    input('Naciśnij Enter, aby kontynuować.')
    
system('cls')
print('To już wszyscy.')
input('Naciśnij Enter, aby kontynuować.')
        