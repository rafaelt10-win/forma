import time
import datetime
import json

data = datetime.date.today()

class WybranyDzien:
    def __init__(self, data):
        self.data = data
        self.posilki = []
        self.treningi = []


    def zwrocSlownik(self):
        return {
            'data': self.data,
            'posilki': self.posilki,
            'treningi': self.treningi,
        }

    def dodajPosilek(self, nazwa, kalorie, bialko):
        self.posilki.append(
            {'nazwa': nazwa,
             'kalorie': kalorie,
             'bialko': bialko}
        )

    def dodajTrening(self, nazwa, powtorzenia, ciezar):
        self.treningi.append(
            {'nazwa': nazwa,
             'powtorzenia': powtorzenia,
             'ciezar': ciezar}
        )

    def zapisDoPliku(self):
        with open('dane.json', 'r', encoding='utf-8') as file:
            dane = json.load(file)

        dane[self.data] = {
            "posilki": self.posilki,
            "treningi": self.treningi,
        }

        with open('dane.json', 'w', encoding='utf-8') as file:
            json.dump(dane, file, indent=2)


    def zwrocRaport(self):
        spozyteKalorie = 0
        spozyteBialko = 0
        calkowiteObciazenie = 0
        with open('dane.json', 'r', encoding='utf-8') as file:
            dane = json.load(file)
            potrzebneDane = dane[self.data]
            for i in range(len(potrzebneDane['posilki'])):
                spozyteKalorie += potrzebneDane['posilki'][i]['kalorie']
                spozyteBialko += potrzebneDane['posilki'][i]['bialko']

            for i in range(len(potrzebneDane['treningi'])):
                calkowiteObciazenie += (potrzebneDane['treningi'][i]['ciezar'] * potrzebneDane['treningi'][i]['powtorzenia'])

        print(f"""
Raport z dnia: {self.data}
Spożyto {spozyteKalorie} kcal, {spozyteBialko} gram białka, a całkowite obiciążenie wyniosło: {calkowiteObciazenie}!
""")
        input('Naciśnij Enter aby wrócić...')


##################################

def ZmianaDaty():
    while True:
        try:
            rok = int(input('Podaj rok: '))
            miesiac = int(input('Podaj miesiąc: '))
            dzien = int(input('Podaj dzień: '))

            nowa_data = datetime.date(rok, miesiac, dzien)
            return nowa_data
        except ValueError:
            print('Błąd! Spróbuj ponownie!')
            continue




choice = input(f'Dzisiaj jest {data}, napisz TAK, jeśli chcesz zmienić datę: ')
if choice == 'TAK':
    data = ZmianaDaty()





print(f'Resetuję datę {data}...')
time.sleep(2)
obiekt = WybranyDzien(str(data))
print(f'Pomyślnie zresetowano!')
time.sleep(1)
while True:

    print(f"""
    {data}
1. Dodaj posiłek
2. Zapisz serię treningową
3. Wygeneruj raport dzienny
4. Zakończ
""")
    wybor = input('Wybierz jedna z opcji: ')
    match wybor:
        case '1':
            try:
                nazwa_posilku = input('Podaj nazwę posiłku: ')
                kalorie = int(input('Podaj kalorie: '))
                bialko = int(input('Podaj ilosc białka: '))
                obiekt.dodajPosilek(nazwa_posilku, kalorie, bialko)
                print('Pomyślnie dodano posiłek!')
                time.sleep(1)
            except ValueError:
                print('Błąd! Spróbuj ponownie!')


        case '2':
            try:
                nazwa_ćwiczenia = input('Podaj nazwę ćwiczenia: ')
                powtorzenia = int(input('Podaj powtorzenia: '))
                ciezar = int(input('Podaj ciezar: '))
                obiekt.dodajTrening(nazwa_ćwiczenia, powtorzenia, ciezar)
                print('Pomyślnie dodano trening!')
                time.sleep(1)
            except ValueError:
                print('Błąd! Spróbuj ponownie!')


        case '3':

            obiekt.zwrocRaport()

        case '4':
            print('Żegnaj!')
            break
        case _:
            print('Nie ma takiej opcji!')
            continue
    obiekt.zapisDoPliku()

