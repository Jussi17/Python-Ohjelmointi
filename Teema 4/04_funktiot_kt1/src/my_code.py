"""
KT1


Tee ohjelma, jossa kysytään KysyJaTestaaLuku() nimisessä funktiossa  käyttäjältä kokonaisluku. 

Funktio palauttaa kokonaislukuarvon seuraavasti:

 

1, jos syötetty luku on positiivinen.
0, jos syötetty luku on nolla.

-1, jos syötetty luku on negatiivinen. 

 

Tulosta näiden paluuarvojen perusteella pääohjelmassa ilmoitus ruudulle.


”Luku oli positiivinen”, jos paluuarvo oli 1.
”Luku oli nolla”, jos paluuarvo oli 0
”Luku oli negatiivinen”, jos paluuarvo oli -1.

"""

#Write KysyJaTestaaLuku function here!
def KysyJaTestaaLuku():
    paluuarvo = 0
    luku = int(input("Anna kokonaisluku: "))
    if luku > 0:
        paluuarvo = 1
    elif luku == 0:
        paluuarvo = 0
    else:
        paluuarvo = -1

    return paluuarvo


if __name__ == "__main__":
    #Write main program below this line
    arvo = KysyJaTestaaLuku()
    if arvo > 0:
        print("Luku oli positiivinen")
    elif arvo == 0:
        print("Luku oli nolla")
    else:
        print("Luku oli negatiivinen")

