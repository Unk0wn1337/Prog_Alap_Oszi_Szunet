import math


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
def hatodikFeladat():
    szam:int = int(input("Szeretnek kerni egy szamot aminek kiszamolom a gyoket: "))
    if szam <= 0:
        print("HIBA: nem lehet negativ vagy 0")
    else:
        print("A szam gyoke",math.sqrt(szam))

def hetedikFeladat():
    szamA: float = float(input("Szeretnek kerni valos szamot: "))
    szamB: float = float(input("Szeretnek kerni valos szamot: "))
    if szamA <= 0 or szamB <= 0:
        print("Hiba: a téglalap oldalai nem pozitívak!")
    else:
        terulet = szamA * szamB
        kerulet = 2 * (szamA+szamB)
        print(f"Terulet: {round(terulet,2)}")
        print(f"Kerulet: {round(kerulet,2)}")

def nyolcadikFeladat():
    print("Udvozoljuk a vadaszati es termewszeti vilagkiallittason! Valasz szektort!")
    szektor:str = str(input("Szektor: "))
    if szektor.isalpha():
        if szektor == 'A' or szektor == 'a':
            print("Nemzetközi Csarnok, World Conservation Forum 2021")
        elif szektor == 'B' or szektor == 'b' or szektor == 'E' or szektor == 'e':
            print("esetén a Kereskedelmi Csarnok, World Conservation Forum 2021")
        elif szektor == 'C' or szektor == 'c':
            print("Konferencia-központ Innovációs Showroom")
        elif szektor == 'D' or szektor == 'd':
            print("Hal, Víz és Ember")
        elif szektor == 'F' or szektor == 'f':
            print("Hagyományos Vadászati Módok Csarnoka")
        elif szektor == 'G' or szektor == 'g':
            print("Hazai és nemzetközi Trófeakiállítás, 12. Nyílt Európai Taxiderma-bajnokság, Vadászat 21.században kiállítás")
        elif szektor == 'H' or szektor == 'h':
            print("Központi Magyar Kiállítás")
        else:
            print("Forduljon a penztarhoz")
    else:
        print("HIBA: Adjon meg egy betut A-H-ig!")
# 8-as feladat
def kilencedikFeladat():
    index = 0
    szam =0
    while index < 10:
        szam +=1
        print(szam * 10)
        index+=1
# 9-as feladat
def tizedikFeladat():
    darab = 0
    vanEA = 0
    leghosszabNev = ""
    nevMegadas:str = str(input("Adj meg egy nevet: "))
    while not nevMegadas == '@':
        if nevMegadas[0] == 'a' or nevMegadas[0] == 'A':
            vanEA +=1
        if len(nevMegadas) > len(leghosszabNev):
            leghosszabNev = nevMegadas
        darab+=1
        nevMegadas: str = str(input("Adj meg egy nevet: "))

    print("ennyi darab nev szuletett:",darab)
    if vanEA > 0:
        print("Van benne a betuvel kezdodo meghozza, ennyi:",vanEA)
    else:
        print("Nincsen benne A betuvel kezdodo :(")

    if len(nevMegadas) > 0:
        print(f"Leghosszabb nev: {leghosszabNev}")
    else:
        print("Semmit nem adtal meg!")

def tizenegyesFeladat():
    index:int = 0
    fej = 0
    iras = 0
    legjSor = 0
    jelSor = 0
    while index < 10:
        erme:str = str(input("I vagy F: "))
        if erme == 'i' or erme == 'I':
            iras+=1
            jelSor +=1
        else:
            jelSor = 0
        if erme == 'f' or erme == 'F':
            fej+=1
            jelSor +=1
        else:
            jelSor = 0
        if jelSor > legjSor:
            legjSor = jelSor
        index+=1
    print("Ennyi fej:",fej)
    print("Leghosszabb sorozat",legjSor)

