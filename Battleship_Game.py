import random

zasady = """
############################################
#               GRA W STATKI               #
############################################

Cel gry:
Twoim zadaniem jest zlokalizowanie i zatopienie wszystkich statków
przeciwnika na planszy 5x5. Każdy statek zajmuje określoną ilość pól
i może być ustawiony poziomo lub pionowo.

Rozgrywka:
1. Na początku gry, komputer losowo rozmieszcza swoje statki.
2. Podajesz współrzędne strzału w formacie: wiersz, kolumna.
3. Możliwe wyniki strzału:
   💥 Trafienie w statek przeciwnika
   ❌ Pudło (nie trafiłeś w żaden statek)
   ⚓ Zatopienie statku (trafiono ostatnie pole danego statku)
4. Gra kończy się, gdy wszystkie statki zostaną zatopione.

Instrukcje dodatkowe:
- Współrzędne wiersza podawaj literą A-E.
- Współrzędne kolumny podawaj liczbą 1-5.
- Staraj się przewidywać ruchy przeciwnika i planować swoje strzały strategicznie!

Powodzenia! 🎯"""

print(zasady)

plansza = [["  ", "  ", "  ", "  ", "  "],
           ["  ", "  ", "  ", "  ", "  "],
           ["  ", "  ", "  ", "  ", "  "],
           ["  ", "  ", "  ", "  ", "  "],
           ["  ", "  ", "  ", "  ", "  "]]

pustaPlansza = [["  ", "  ", "  ", "  ", "  "],
           ["  ", "  ", "  ", "  ", "  "],
           ["  ", "  ", "  ", "  ", "  "],
           ["  ", "  ", "  ", "  ", "  "],
           ["  ", "  ", "  ", "  ", "  "]]

def wypisaniePlanszy(plansza):
        print("\n")
        print("     1    2    3    4    5 ")
        print("   ──── ──── ──── ──── ──── ")
        for i in range(5):
            for j in range(5):
                if j == 0:
                     print(f"{chr(65+i)} | {plansza[i][j]}", end=" |")
                else:
                     print(f" {plansza[i][j]}", end=" |")
            print()
            print("   ──── ──── ──── ──── ──── ")
        print("\n")

wypisaniePlanszy(plansza)

orientacjaStatku = ["pionowy", "poziomy"]

statki = []

def rozmieszczenieDanegoStatku(plansza, dlugosc, orientacjaStatku, statki):
    statek = []
    while True:
        orientacja = orientacjaStatku[random.randint(0, 1)]
        if orientacja == "poziomy":
            wiersz = random.randint(0, 4)
            kolumna = random.randint(0, 5 - dlugosc)
            wolne = True
            for i in range(dlugosc):
                if plansza[wiersz][kolumna + i] != "  ":
                    wolne = False
                    break
            if wolne:
                for i in range(dlugosc):
                    plansza[wiersz][kolumna + i] = "🚢"
                    statek.append((wiersz, kolumna + i))
                break
        if orientacja == "pionowy":
            wiersz = random.randint(0, 5 - dlugosc)
            kolumna = random.randint(0, 4)
            wolne = True
            for i in range(dlugosc):
                if plansza[wiersz + i][kolumna] != "  ":
                    wolne = False
                    break
            if wolne:
                for i in range(dlugosc):
                    plansza[wiersz + i][kolumna] = "🚢"
                    statek.append((wiersz + i, kolumna))
                break
    statki.append(statek)
    return statek

potrojnyStatek = rozmieszczenieDanegoStatku(plansza, 3, orientacjaStatku, statki)
podwojnyStatek = rozmieszczenieDanegoStatku(plansza, 2, orientacjaStatku, statki)
pojedynczyStatek = rozmieszczenieDanegoStatku(plansza, 1, orientacjaStatku, statki)

def czyTrafione(plansza, wiersz, kolumna):
     if pustaPlansza[ord(wiersz.upper()) - 65][kolumna - 1] == "💥" or pustaPlansza[ord(wiersz.upper()) - 65][kolumna - 1] == "❌":
          return None
     if plansza[ord(wiersz.upper()) - 65][kolumna - 1] == "🚢":
          pustaPlansza[ord(wiersz.upper()) - 65][kolumna - 1] = "💥"
          return True
     pustaPlansza[ord(wiersz.upper()) - 65][kolumna - 1] = "❌"
     return False

def czyZatopione(statek, pustaPlansza):
     for wspolrzedne in statek:
          if pustaPlansza[wspolrzedne[0]][wspolrzedne[1]] != "💥":
               return False
     return True

trafienia = 0
strzaly = 0
zatopionyPotrojny = False
zatopionyPodwojny = False
zatopionyPojedynczy = False
while trafienia < 6:
     while True:
          wiersz = input("Podaj wiersz: ")
          kolumna = int(input("Podaj kolumne: "))
          if wiersz.upper() not in ["A", "B", "C", "D", "E"] or kolumna not in [1, 2, 3, 4, 5]:
               print("Nieprawidłowe współrzędne. Spróbuj ponownie.")
          else:
               break
     wynik = czyTrafione(plansza, wiersz, kolumna)
     if wynik == None:
          print("🔄 To pole już zostało sprawdzone. Wybierz inne! ")
     elif wynik == True:
          print("💥 Trafiony! ")
          trafienia += 1
          strzaly += 1
          if zatopionyPotrojny == False and czyZatopione(potrojnyStatek, pustaPlansza) == True:
               print("⚓ Zatopiłeś potrójny statek! ")
               zatopionyPotrojny = True
          elif zatopionyPodwojny == False and czyZatopione(podwojnyStatek, pustaPlansza) == True:
               print("⚓ Zatopiłeś podwójny statek! ")
               zatopionyPodwojny = True
          elif zatopionyPojedynczy == False and czyZatopione(pojedynczyStatek, pustaPlansza) == True:
               print("⚓ Zatopiłeś pojedynczy statek! ")
               zatopionyPojedynczy = True
     elif wynik == False:
          print("❌ Pudło! ")
          strzaly += 1
     wypisaniePlanszy(pustaPlansza)

print(f"🏆 Gratulacje! Wygrałeś grę - wszystkie statki przeciwnika zostały zatopione w {strzaly} strzałach! ")