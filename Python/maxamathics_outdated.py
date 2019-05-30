# (c) Max Spiekermann, 2016
# Made by the 15-years old developer Max Spiekermann from Germany

def addition (*args):

    allargs = []
    ganzezahlsumme = 0
    kommazahlsumme = 0
    längstekzahlen = 0

    for n in args:
        allargs.append(str(n))

    for zahl in allargs:
        zahl =list(zahl)
        ganzezahl = ""
        kommazahl = ""

        for zeichenganz in zahl[0:zahl.index(".")]:
            ganzezahl = ganzezahl+zeichenganz

        ganzezahlsumme = ganzezahlsumme+int(ganzezahl)

        for zeichenkomma in zahl[zahl.index(".")+1:]:
            kommazahl = kommazahl+zeichenkomma
            if (len(list(kommazahl))>längstekzahlen):
                längstekzahlen = len(list(kommazahl))

    for zahl in allargs:

        kommazahl = ""

        for zeichenkomma in zahl[zahl.index(".")+1:]:
            kommazahl = kommazahl+zeichenkomma

        for c in range (0, längstekzahlen-len(list(kommazahl))):
            kommazahl = kommazahl+"0"

        kommazahlsumme = kommazahlsumme+int(kommazahl)

    kommazahlsumme = list (str(kommazahlsumme))
    kommazahlsumme.insert(len(kommazahlsumme)-längstekzahlen, ".")
    kommazahlsumme = ''.join(kommazahlsumme)
    kommazahlsumme = float(kommazahlsumme)
    total =kommazahlsumme+ganzezahlsumme

    return total


# Retruns wether a 'num' is devidable by 'devidable'
def devidable (num, devidable):
    math = num/devidable
    #
    math1 = int(math)
    if (math1 != math):
        math1 = float
    else:
        math1 = int
    #
    if (math1 == int):
        print (type(math))
        return True
    else:
        return False
