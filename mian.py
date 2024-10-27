import random

def gra_w_zgadywanie():
    liczba_do_odgadniecia = random.randint(1, 100)
    proba = 0
    max_proby = 4


    print("zgadnij liczbę od 1 do 100, masz maksymalnie 5 prób")
    print(liczba_do_odgadniecia)


    while True:
        proba += 1
        reszta = max_proby - proba
        odpowiedz = int(input("wpisz swoją liczbę: "))
        if odpowiedz > 100:
            print("liczba wykracza poza schemat")
            continue

        if odpowiedz < liczba_do_odgadniecia:
            print("|za mało!|")
        elif odpowiedz > liczba_do_odgadniecia:
            print("|za dużo!|")
        else:
            print("|Brawo zgadłeś liczbę!|")
            break

        if proba < max_proby:
            if reszta == 1:
                print("została ci ostatnia próba")
            else:
                print(f"liczba prób które ci zostały wynosi: |{reszta}|")

        elif proba >= max_proby:
            print("przegrałeś")

            break

gra_w_zgadywanie()
