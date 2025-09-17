plansza = [[" ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " "]]

def wypisaniePlanszy(plansza):
        print("\n")
        print("    1   2   3   4   5 ")
        print("   ─── ─── ─── ─── ─── ")
        for i in range(5):
            for j in range(5):
                if j == 0:
                     print(f"{chr(65+i)} | {plansza[i][j]}", end=" |")
                else:
                     print(f" {plansza[i][j]}", end=" |")
            print()
            print("   ─── ─── ─── ─── ─── ")
        print("\n")

wypisaniePlanszy(plansza)