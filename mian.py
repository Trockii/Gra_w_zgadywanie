import random

def gra_w_zgadywanie():
    liczba_do_odgadniecia = random.randint(1, 100)
    proba = 0
    max_proby = 5
    prz = liczba_do_odgadniecia % 2 == 0
    nprz = liczba_do_odgadniecia % 2 != 0

    print("Zgadnij liczbę od 1 do 50, masz maksymalnie 5 prób")

    while True:
        proba += 1
        reszta = max_proby - proba
        odpowiedz = int(input("Wpisz swoją liczbę: "))
        if odpowiedz > 50 or odpowiedz < 1:
            print("Liczba wykracza poza schemat, wpisz liczbę od 1 do 50")
            continue

        if odpowiedz < liczba_do_odgadniecia:
            print("|Za mało!|")
        elif odpowiedz > liczba_do_odgadniecia:
            print("|Za dużo!|")
        else:
            print("|Brawo zgadłeś liczbę!|")
            break

        if proba < max_proby:
            if reszta == 1:
                print("Została ci ostatnia próba")
            if prz and reszta == 1:
                print("Liczba jest parzysta")
            elif nprz:
                print("Liczba jest nieparzysta")
            else:
                print(f"Liczba prób, które ci zostały, wynosi: |{reszta}|")
        else:
            print(f"Przegrałeś, liczbą do odgadnięcia była liczba {liczba_do_odgadniecia}")
            break

gra_w_zgadywanie()
