# -*- coding: utf-8 -*-

"""
KT 4

Kysy käyttäjältä lukujjen määrä ja arvo annettu  kplmäärä  liukulukuja väliltä 1 – 100.
Arvo luku seuraavasti:
    random_decimal = random.randint(100, 10000) / 100
Tulosta arvottu luku käyttäjälle (samalle riville kuin edellinen välilyönnillä erotettuna) ja kirjoita se arvot.txt tiedostoon allekkain.
Jos syötetty luku on < 1, ei ohjelma päättyy ja tulostuu "Virhe!".

Jos tiedosto on jo olemassa, vanhat tiedot menetetään
Älä käytä listaa tms tässä vaiheessa vaan vie luku tiedostoon heti, kun se on arvottu.
Sen jälkeen lue arvot tiedostosta listaan ja lajittele se. Tämän jälkeen tulosta listan  arvot sekä vie
lukujen kplmäärä, summa, keskiarvo, minimiarvo ja maksimiarvo tulokset.txt -tiedostoon
oheisen mallin mukaisesti kahdella desimaalilla (pl kpl):
Kpl: 2
Sum:5.00
Ka: 2.50
Min: 1.00
Max:4.00

Ohessa ajoesimerkki:

Montako lukua arvotaan? 3
Arvottiin seuraavat luvut ja talletetaan tiedostoon arvot.txt:
75.41 12.84 17.27
Luettiin seuraavat luvut (lajiteltuna) tiedostosta arvot.txt:
12.84 17.27 75.41
Ja lopuksi  tiedostosta tulokset.txt löytyy seuraavat tiedot:
Lkm: 3
Sum: 105.52
Ka: 35.17
Min: 12.84
Max: 75.41

Ole taas huolellinen tulostusten kanssa!

"""
import random

maara = int(input("Montako lukua arvotaan? "))
if maara < 1:
    print("Virhe!")
    exit()

print("Arvottiin seuraavat luvut ja talletetaan tiedostoon arvot.txt:")

with open("arvot.txt", "w") as tiedosto:
    for i in range(maara):
        random_decimal = random.randint(100, 10000) / 100
        print(f"{random_decimal:.2f}", end=" ")
        tiedosto.write(f"{random_decimal:.2f}\n")
print()

luvut = []
with open("arvot.txt", "r") as tiedosto:
    for rivi in tiedosto:
        luvut.append(float(rivi.strip()))
lv_sorted = sorted(luvut)

print("Luettiin seuraavat luvut (lajiteltuna) tiedostosta arvot.txt:")
print(" ".join(f"{l:.2f}" for l in lv_sorted))

with open("tulokset.txt", "w") as tiedosto:
    tiedosto.write(f"Lkm: {len(lv_sorted)}\n")
    tiedosto.write(f"Sum: {sum(lv_sorted):.2f}\n")
    tiedosto.write(f"Ka: {sum(lv_sorted) / len(lv_sorted):.2f}\n")
    tiedosto.write(f"Min: {min(lv_sorted):.2f}\n")
    tiedosto.write(f"Max: {max(lv_sorted):.2f}\n")

print("Ja lopuksi tiedostosta tulokset.txt löytyy seuraavat tiedot:")
print(f"Lkm: {len(lv_sorted)}")
print(f"Sum: {sum(lv_sorted):.2f}")
print(f"Ka: {sum(lv_sorted) / len(lv_sorted):.2f}")
print(f"Min: {min(lv_sorted):.2f}")
print(f"Max: {max(lv_sorted):.2f}")

