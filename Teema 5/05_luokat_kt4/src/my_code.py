"""
KT4

Pääset suunnittelemaan Tuote-sovellusta suuren kauppaketjun tuotekehitysosastolla. Tehtävänäsi on suunnitella luokkarakenne, jolla voidaan hallinnoida yrityksen tuotteita. Kaikilla tuotteilla on samat yhteiset ominaisuudet: nimi, hinta, hyllypaikka sekä koodi. Nämä esitellään tuote-luokassa, jonka aliluokat perivät. Aliluokkia on kolme, joilla on omia ominaisuuksia:

a.                         vaate: koko, materiaali
b.                         ruoka: maa, paivays
c.                         kodinkone: takuu, paino 

Tee yksinkertainen ohjelma, jolla voit syöttää tuotteita yhdelle tuotelistalle sekä tulostaa koko listan sisällön. Luokkien jäsenmuuttujien tyyppejä ei ole määritelty eli saat päättää ne itse. Ohjelmassa ensin valitaan minkä tyyppistä tuotetta ollaan syöttämässä, jonka jälkeen tiedot täytetään. Miten lopetat syötön on sinun päätettävissä. Tietysti lopuksi lista tulostetaan.

Ohessa esimerkkiajo:

Mikä tuote lisätään listaan (1 = Ruoka, 2 = Vaate, 3 = Kodinkone, muu = Lopetus: 1
Anna tuotteen nimi: Sokeri
Anna hinta: 2.45
Anna hyllypaikka: Ruoka 11
Anna koodi: 111-222-333-22
Ruuan alkuperämaa: Tanska
Päiväys: 1.3.2024

Mikä tuote lisätään listaan (1 = Ruoka, 2 = Vaate, 3 = Kodinkone, muu = Lopetus: 2
Anna tuotteen nimi: Paita
Anna hinta: 22.10
Anna hyllypaikka: Vaate 3
Anna koodi: 222-122-232-11
Vaatteen koko: M
Vaatteen materiaali: Puuvilla

Mikä tuote lisätään listaan (1 = Ruoka, 2 = Vaate, 3 = Kodinkone, muu = Lopetus: 3
Anna tuotteen nimi: Pakastin
Anna hinta: 320.00
Anna hyllypaikka: Varasto 12
Anna koodi: 543-234-232-22
Kodinkoneen takuu: 1 vuosi
Kodinkoneen paino: 100kg

Mikä tuote lisätään listaan (1 = Ruoka, 2 = Vaate, 3 = Kodinkone, muu = Lopetus: l

Nimi:       Sokeri
Hinta:      2.45
Hylly:      Ruoka 11
Koodi:      111-222-333-22
Alkuperä:   Tanska
Päiväys:    1.3.2024

Nimi:       Paita
Hinta:      22.10
Hylly:      Vaate 3
Koodi:      222-122-232-11
Koko:       M
Materiaali: Puuvilla

Nimi:       Pakastin
Hinta:      320.00
Hylly:      Varasto 12
Koodi:      543-234-232-22
Takuu:      1 vuosi
Paino:      100kg

"""

from datetime import datetime


class tuote:
    def __init__(self, nimi: str, hinta: float, hyllypaikka: str, koodi: str):
        self.nimi = nimi
        self.hinta = hinta
        self.hyllypaikka = hyllypaikka
        self.koodi = koodi

    def __str__(self):
        return f"Nimi: {self.nimi}\nHinta: {self.hinta:.2f}\nHylly: {self.hyllypaikka}\nKoodi: {self.koodi}"


class vaate(tuote):
    def __init__(self, nimi, hinta, hyllypaikka, koodi, koko, materiaali):
        super().__init__(nimi, hinta, hyllypaikka, koodi)
        self.koko = koko
        self.materiaali = materiaali

    def __str__(self):
        return super().__str__() + f"\nKoko: {self.koko}\nMateriaali: {self.materiaali}"


class ruoka(tuote):
    def __init__(self, nimi, hinta, hyllypaikka, koodi, maa, paivays):
        super().__init__(nimi, hinta, hyllypaikka, koodi)
        self.maa = maa
        self.paivays = datetime.strptime(paivays, "%d.%m.%Y")

    def __str__(self):
        formatted_pvm = self.paivays.strftime('%d.%m.%Y').lstrip("0").replace(".0", ".")
        return super().__str__() + f"\nAlkuperä: {self.maa}\nPäiväys: {formatted_pvm}"


class kodinkone(tuote):
    def __init__(self, nimi, hinta, hyllypaikka, koodi, takuu, paino):
        super().__init__(nimi, hinta, hyllypaikka, koodi)
        self.takuu = takuu
        self.paino = paino

    def __str__(self):
        return super().__str__() + f"\nTakuu: {self.takuu}\nPaino: {self.paino}"


def main():
    tuotteet = []
    while True:
        tavara = input("Mikä tuote lisätään listaan (1 = Ruoka, 2 = Vaate, 3 = Kodinkone, muu = Lopetus): ")
        if tavara not in ("1", "2", "3"):
            break

        nimi = input("Anna tuotteen nimi: ")
        hinta = float(input("Anna hinta: "))
        hylly = input("Anna hyllypaikka: ")
        koodi = input("Anna koodi: ")

        if tavara == "1":
            maa = input("Ruuan alkuperämaa: ")
            paivays = input("Päiväys (pp.kk.vvvv): ")
            tuotteet.append(ruoka(nimi, hinta, hylly, koodi, maa, paivays))
        elif tavara == "2":
            koko = input("Vaatteen koko: ")
            materiaali = input("Vaatteen materiaali: ")
            tuotteet.append(vaate(nimi, hinta, hylly, koodi, koko, materiaali))
        elif tavara == "3":
            takuu = input("Kodinkoneen takuu: ")
            paino = input("Kodinkoneen paino: ")
            tuotteet.append(kodinkone(nimi, hinta, hylly, koodi, takuu, paino))

    print("\nTallennetut tuotteet:\n")
    for tuote in tuotteet:
        print(tuote, "\n")


if __name__ == "__main__":
    main()

