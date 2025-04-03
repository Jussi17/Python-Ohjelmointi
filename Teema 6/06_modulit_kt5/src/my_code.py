"""
KT5

Korjaa alla oleva funktio siten, että se palauttaa 'Olen antanut palautteen'

"""
#imports here

def palautteen_tila():
    return 'Olen antanut palautteen'

if __name__ == "__main__":
    palaute = palautteen_tila()
    palaute2 = "Hyvä kurssi, olin jo aikaisemmin kokenut Pythonin käyttäjä, mutta opin silti uutta ja pidin videoista"
    print(f"{palaute}\n{palaute2}")


