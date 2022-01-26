import random

plocha = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
vyherca = None
aktualny_hrac = "X"
hra_bezi = True
#clovek = X
#pc = O

#vykreslenie hracej plochy
def hracia_plocha(plocha):
    print(str(plocha[0]) + " | " + str(plocha[1]) + " | " + str(plocha[2]))
    print("----------")
    print(str(plocha[3]) + " | " + str(plocha[4]) + " | " + str(plocha[5]))
    print("----------")
    print(str(plocha[6]) + " | " + str(plocha[7]) + " | " + str(plocha[8]))


# hrac - clovek
def clovek(plocha):
    tah = int(input("Zadaj cislo okienka: "))
    if plocha[tah - 1] == " ":
        plocha[tah - 1] = "X"
    else:
        print("Toto pole je už obsadené")


# hrac - pc
def pc(plocha):
    while aktualny_hrac == "O":
        tah = random.randint(0, 9)
        if plocha[tah - 1] == " ":
            plocha[tah - 1] = "O"
            zmena_hracov()

#zmeni hracov
def zmena_hracov():
    global aktualny_hrac
    if aktualny_hrac == "X":
        aktualny_hrac = "O"
    elif aktualny_hrac == "O":
        aktualny_hrac = "X"


# skontroluje ci su v riadku 3 rovnake znaky za sebou
def kontrola_riadkov(plocha):
    global vyherca
    global hra_bezi
    for i in range(0, 3, 3):
        if plocha[i] == plocha[i + 1] == plocha[i + 2] and plocha[i] != " ":
            vyherca = plocha[i]
            return True


# skontroluje ci su v stlpci 3 rovnake znaky za sebou
def kontrola_stlpcov(plocha):
    global vyherca
    global hra_bezi
    for i in range(3):
        if plocha[i] == plocha[i + 3] == plocha[i + 6] and plocha[i] != " ":
            vyherca = plocha[i]
            return True


# skontroluje ci su v diagonale 3 rovnake znaky za sebou
def kontrola_diagonaly(plocha):
    global vyherca
    if plocha[0] == plocha[4] == plocha[8] and plocha[4] != " ":
        vyherca = plocha[0]
        return True
    elif plocha[2] == plocha[4] == plocha[6] and plocha[4] != " ":
        vyherca = plocha[2]
        return True


# overi vyhru
def kontrola_vyhry(plocha):
    global hra_bezi
    if kontrola_riadkov(plocha):
        hracia_plocha(plocha)
        print("Gratulujem, vyhráva hráč", vyherca)
        hra_bezi = False
    elif kontrola_stlpcov(plocha):
        hracia_plocha(plocha)
        print("Gratulujem, vyhráva hráč", vyherca)
        hra_bezi = False
    elif kontrola_diagonaly(plocha):
        hracia_plocha(plocha)
        print("Gratulujem, vyhráva hráč", vyherca)
        hra_bezi = False


# overi ci su este nejake policka "volne"
def kontrola_policok(plocha):
    global hra_bezi
    if " " not in plocha:
        hracia_plocha(plocha)
        print("Koniec hry, všetky políčka sú obsadené!")
        hra_bezi = False

# spustenie celej hry v konzole
while hra_bezi:
    hracia_plocha(plocha)
    clovek(plocha)
    kontrola_vyhry(plocha)
    kontrola_policok(plocha)
    zmena_hracov()
    pc(plocha)
    kontrola_vyhry(plocha)
    kontrola_policok(plocha)
