import random

plansza = [["  ", "  ", "  ", "  ", "  "],
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

def rozmieszczenieStatkow(plansza, orientacjaStatku):
     orientacja = orientacjaStatku[random.randint(0, 1)]
     if orientacja == "poziomy":
          wiersz = random.randint(0, 4)
          kolumna = random.randint(0, 5 - 3) #(3, to jest dlugosc statku)
          for i in range(3):
               plansza[wiersz][kolumna - 1 + i] = "🚢"
     elif orientacja == "pionowy":
          wiersz = random.randint(0, 5 - 3)
          kolumna = random.randint(0, 4)
          for i in range(3):
               plansza[wiersz + i][kolumna - 1] = "🚢"

rozmieszczenieStatkow(plansza, orientacjaStatku)

def czyTrafione(plansza, wiersz, kolumna):
     if plansza[ord(wiersz.upper()) - 65][kolumna - 1] == "🚢":
          plansza[ord(wiersz.upper()) - 65][kolumna - 1] = "💥"
          return True
     plansza[ord(wiersz.upper()) - 65][kolumna - 1] = "❌"
     return False

trafienia = 0
while trafienia < 3:
     wiersz = input("Podaj wiersz: ")
     kolumna = int(input("Podaj kolumne: "))
     if czyTrafione(plansza, wiersz, kolumna) == True:
          print("Trafiony! ")
          trafienia += 1
     else:
          print("Pudło! ")
     wypisaniePlanszy(plansza)


print("Wygrałeś! Zatopiłeś wszystkie statki! ")