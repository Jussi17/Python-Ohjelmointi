"""
KT4

Kirjoita funktio Tsekkaus, joka tulostaa ensin tiedon siitä, kuinka monta parametria funktioon tuli. Eli parametrien määrää ei ole rajattu. Jos ensimmäisen parametri oli "opettaja" niin funktio tulosta seuraavalle riville "Koita saada oppilaat oppimaan", jos se taas oli "opiskelija", niin funktio tulostaa "Koita opiskella ahkerasti". Jos parametri oli jotain muuta, niin funktio tulostaa "En ymmarra". Jos parametreja ei ole yhtään, niin funktio tulostaa "Virhe".

"""
#Write functions and define global variables here!
def Tsekkaus(*args):
    print(f"Parametreja tuli: {len(args)}")

    if len(args) == 0:
        print("Virhe")
    elif len(args) > 0:
        if args[0] == "opettaja":
            print("Koita saada oppilaat oppimaan")
        elif args[0] == "opiskelija":
            print("Koita opiskella ahkerasti")
        else:
            print("En ymmarra")


if __name__ == "__main__":
    #Write main program below this line
    Tsekkaus()
    Tsekkaus("opettaja")
    Tsekkaus("opiskelija")
    Tsekkaus("jotain muuta")
    Tsekkaus("opettaja", "opiskelija")
    Tsekkaus("opiskelija", "opettaja")