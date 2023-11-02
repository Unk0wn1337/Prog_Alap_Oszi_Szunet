def elsoFeladat():
    szam:int = int(input("Szeretnek kerni egy szamot 200 es 920 kozott: "))
    if szam >= 200 and szam <= 920:
        print(szam)
    else:
        print("HIBA: nem 200 es 920 kozott van a szam")

def masodikFeladat(szam):
    ezres:int = 0
    szazas:int = 0
    tizes:int = 0
    egyes:int = 0
    if szam >= 1000:
        ezres = szam // 1000
        szam = szam % 1000
    if szam >= 100:
        szazas = szam // 100
        szam = szam % 100
    if szam >= 10:
        tizes = szam // 10
        szam = szam % 10
    if szam >= 1:
        egyes = szam // 1

    print(f"Ezres {ezres} db")
    print(f"Szazas {szazas} db")
    print(f"Tizes {tizes} db")
    print(f"Egyes {egyes} db")



def harmadikFeladat(szam):
   osszeg:int = 0
   szamToString = str(szam)
   for i in szamToString:
       if i.isdigit():
           osszeg += int(i)
   print(f"Osszeguk: {osszeg}")


def negyedikFeladat(a):
    if a < 0:
        print("HIBA: nem lehet negativ")
    if a == 0:
        print("Be se jovok!")
    if a == 1:
        print("Meg 90%-on vagyunk")
    if a == 2 or a == 3:
        print("Meg birjuk (60%)")
    if a == 4 or a == 5 or a == 6 or a == 7:
        print("Progit tanulunk, toltodunk! 70%")
    if a == 8 or a == 9:
        print("Lasssan nem birjuk tovabb! 50%")
    if a >= 10:
        print("Ez mar tenyleg tulzas")

def otodikFeladat(nap,ora):
    if nap == "Hetfo":
        print("Marti perpillanat alszik")
    elif nap == "Kedd":
        if ora == "hittan":
            print("figyel")
        else:
            print("alszik")
    elif nap == "Szerda":
        if ora == "programozas":
            print("Marti dolgozik")
        else:
            print("nincs info")
    elif nap == "Csutortok":
        print("figyel")
    elif nap == "Pentek":
        print("felig van jelen")



