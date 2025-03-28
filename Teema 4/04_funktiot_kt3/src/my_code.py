"""
KT3
Tee ohjelma, joka laskee mäkihyppääjän yhden kierroksen suorituspisteet. Ensin ohjelma kysyy hypyn pituuden (liukuluku 0.5 metrin välein) jonka jälkeen se kysyy viiden arvostelutuomarin tyylipisteet (0-20 välillä 0.5 välein eli esim. 16.5 tai 17.0 tai 18.5). Hyppääjän pisteet muodostuvat kaavasta.

pisteet = (hypyn pituus - kriittinen piste) * 1.8 + kolmen keskimmäisen tuomarin tyylipisteet + 60. 

Tyylipisteissä siis parhain ja huonoin pistemäärä tipahtaa pois.

Ohjelman hyppyrimäen kriittinen piste on 90 metrin kohdalla. Laita kriittinen piste globaaliin vakioon KR_PISTE. Tulosta lopuksi hypyn pituus ja hypyn pisteet. Käytä ohjelmassa funktioita:


KysyHypynPituus - Kysyy hypyn pituuden ja palauttaa sen reaalilukuna
KysyTuomareidenPisteet - Kysyy tuomareiden pisteet yksi kerrallaan. Palauttaa listan jossa on kunkin tuomarin antamat pisteet reaalilukuina. 
LaskeHypynPisteet - Saa ensimmäisenä parametrina hypyn pituuden sekä toisena parametrina listan joka sisältää kaikkien tuomareiden antamat tyylipisteet. Palauttaa hypyn pisteet lukuna.

 
"""
KR_PISTE = 90

def KysyHypynPituus():
    while True:
        try:
            pituus = float(input("Hypyn pituus: "))
            if (pituus * 2) % 1 == 0:
                return pituus
            else:
                print("Virhe: Anna pituus 0.5 metrin välein!")
        except ValueError:
            print("Virhe: Syötä pituus!")

def KysyTuomareidenPisteet():
    pisteet = []
    for i in range(5):
        while True:
            try:
                piste = float(input(f"Tuomarin {i + 1} tyylipisteet (0-20): "))
                if 0 <= piste <= 20 and (piste * 2) % 1 == 0:
                    pisteet.append(piste)
                    break
                else:
                    print("Virhe: Anna pisteet väliltä 0-20 (0.5 välein)")
            except ValueError:
                print("Virhe: Syötä numero!")

    pisteet.sort()
    viralliset_pisteet = sum(pisteet[1:-1])
    return viralliset_pisteet


def LaskeHypynPisteet(mitta, tyyli):
    pisteet = (mitta - KR_PISTE) * 1.8 + tyyli + 60
    return pisteet


if __name__ == "__main__":
    pituus = KysyHypynPituus()
    tyylipisteet = KysyTuomareidenPisteet()
    yhteispisteet = LaskeHypynPisteet(pituus, tyylipisteet)

    print(f"Hypyn pituus: {pituus} m")
    print(f"Hypyn pisteet: {yhteispisteet:.1f}")



