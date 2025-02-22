import random
def is_het_geraden(gok, geheime_nummer):
    if gok == geheime_nummer:
        print('correct')
        return True
    else:
        print('fout')
        return False

def raad_het_getal(bovengrens):
    geheime_nummer = random.randint(1, bovengrens)
    einde_spel = False
    while not einde_spel:
        gok = int(input("geef een getal"))
        geraden = is_het_geraden(gok, geheime_nummer)
        if geraden == True:
            einde_spel = True

raad_het_getal(10)

