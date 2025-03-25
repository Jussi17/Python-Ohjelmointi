# -*- coding: utf-8 -*-
"""

KT4

Lue nimi, pituus ja paino em nimisiin muuttujiin. Käytä juuri noita muuttujanimiä.
Esittele lisäksi bmi muuttuja ja alusta se nollaksi. Kysy käyttäjältä nimi, pituus metreinä ja paino kiloina.
Laske painoindeksi bmi muuttujaan seuraavasti:


bmi = paino / pituus ^ 2



Tulosta lopuksi:


Jussi Juonio pituutesi on 1.81 m ja painosi 104.0 kg
Painoindeksisi on siten 31.75

Huomaa, että bmi tulee kahdella desimaalilla

"""
nimi = input("Anna nimesi: ")
pituus = float(input("Anna pituutesi metreinä: "))
paino = float(input("Anna painosi kiloina: "))
bmi = 0

bmi = paino / pituus**2

print(f"{nimi} pituutesi on {pituus:.2f} m ja painosi on {paino:.1f} kg")
print(f"Painoindeksisi on siten {bmi:.2f}")