# -*- coding: utf-8 -*-

"""

KT5

Kysy käyttäjältä kaksi lukua. Ensimmäisessä luvussa annetaan alkuarvo  lukuparille ja toisessa montako kertaa lukuparia kasvatetaan/vähennetään.


Tulosta lukuparit allekkain for-silmukkaa käyttäen. Vasen luku siis kasvaa ja oikea vähenee yhden verran kullakin rivillä.

Jos käyttäjä antaa luvut 10 ja 5, tulostus näyttää seuraavalta:
10,10
11,9
12,8
13,7
14,6
15,5



Eli tulostuvan lukuparin ensimmäinen arvo kasvaa ja toinen vähenee lähtien liikkeelle luvusta 10 toistuen 5 kertaa

"""
luku = int(input("Anna alkuarvo: "))
kierros = int(input("Monta kertaa kasvatetaan?: "))

vasenluku = luku
oikealuku = luku

for luku in range(kierros + 1):
    print(f"{vasenluku},{oikealuku}")
    vasenluku += 1
    oikealuku -= 1
