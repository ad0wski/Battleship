import random

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

def rozmieszczenieDanegoStatku(plansza, dlugosc, orientacjaStatku):
     while True:
          orientacja = orientacjaStatku[random.randint(0, 1)]
          if orientacja == "poziomy":
               wiersz = random.randint(0, 4)
               kolumna = random.randint(0, 5 - dlugosc)
               for i in range(dlugosc):
                    for j in range(dlugosc):
                         if plansza[wiersz][kolumna + j] != " ":
                              break
                    plansza[wiersz][kolumna + i] = "🚢"
          if orientacja == "pionowy":
               wiersz = random.randint(0, 5 - dlugosc)
               kolumna = random.randint(0, 4)
               for i in range(dlugosc):
                    for j in range(dlugosc):
                         if plansza[wiersz][kolumna + j] != " ":
                              break
                    plansza[wiersz + i][kolumna] = "🚢"
               break

# def rozmieszczenieStatkow(plansza, orientacjaStatku):
#      orientacja = orientacjaStatku[random.randint(0, 1)]
#      if orientacja == "poziomy":
#           wiersz = random.randint(0, 4)
#           kolumna = random.randint(0, 5 - 3) #(3, to jest dlugosc statku)
#           for i in range(3):
#                plansza[wiersz][kolumna + i] = "🚢"
#      elif orientacja == "pionowy":
#           wiersz = random.randint(0, 5 - 3)
#           kolumna = random.randint(0, 4)
#           for i in range(3):
#                plansza[wiersz + i][kolumna] = "🚢"

rozmieszczenieDanegoStatku(plansza, 3, orientacjaStatku)
rozmieszczenieDanegoStatku(plansza, 2, orientacjaStatku)
rozmieszczenieDanegoStatku(plansza, 1, orientacjaStatku)

def czyTrafione(plansza, wiersz, kolumna):
     if pustaPlansza[ord(wiersz.upper()) - 65][kolumna - 1] == "💥" or pustaPlansza[ord(wiersz.upper()) - 65][kolumna - 1] == "❌":
          print("Już strzeliłeś w to miejsce! ")
          return None
     if plansza[ord(wiersz.upper()) - 65][kolumna - 1] == "🚢":
          pustaPlansza[ord(wiersz.upper()) - 65][kolumna - 1] = "💥"
          return True
     pustaPlansza[ord(wiersz.upper()) - 65][kolumna - 1] = "❌"
     return False

trafienia = 0
while trafienia < 6:
     wiersz = input("Podaj wiersz: ")
     kolumna = int(input("Podaj kolumne: "))
     if czyTrafione(plansza, wiersz, kolumna) == True:
          print("Trafiony! ")
          trafienia += 1
     elif czyTrafione(plansza, wiersz, kolumna) == False:
          print("Pudło! ")
     wypisaniePlanszy(pustaPlansza)


print("Wygrałeś! Zatopiłeś wszystkie statki! ")