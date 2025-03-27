# -*- coding: utf-8 -*-

"""
KT 5

Kirjoita Python-kielinen ohjelma, joka kysyy käyttäjän nimeä, kuitenkin enintään 18 merkkiä.
Merkeissä saa olla tyhjeitä. Jos merkkejä > 18, tulostuu teksti "Virhe!".
Ohjelma tulostaa nimen alla kuvatusti laskevana ja pituudesta riippumatta sivusuunnassa alkaen oikeasta reunasta.
Jotta teksti hahmottuisi riviksi, lisää kaksi välilyöntiä perättäisten merkkien väliin. Kirjoita tämä myös nimi.txt-tiedostoon samassa muodossa.

Esimerkkiajo:
Anna nimesi:Jukka
        a
      k
    k
  u
J

"""
nimi = input("Anna nimesi: ")
maara = len(nimi)

if maara > 18:
    print("Virhe!")
    exit()
else:
    with open("nimi.txt", "w") as tiedosto:
        for i in range(len(nimi)):
            oikeareuna = " " * (len(nimi) - i - 1) * 2
            merkki = "  ".join(nimi[-(i+1)])
            rivi = oikeareuna + merkki
            print(rivi)
            tiedosto.write(rivi + "\n")




