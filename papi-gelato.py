from typing import Hashable


bolprijs = 1.10
hoornprijs = 1.25
bakprijs = 0.75


def start():
    space()
    print("--------------------------------------------")
    space()
    print("Welkom bij Papi Gelato")
    space()
    print("--------------------------------------------")
    space()


def ask():
    
    global bolprijs
    global hoornprijs
    global bakprijs
    meerbol = 0
    bol = int(input('hoeveel bolletjes '))
    while bol > 0:
        AantalB = bol
        meerbol + AantalB
        
        
        print(meerbol)

        if bol < 9:
            smaak = welkesmaak(AantalB)
            BofH = BakjeOfHoorn(AantalB)
                                                                                                                                                                                                                                                                                                                                                 
        elif hoeveelbolletjes > 8:
            print("zulke grote baken hebbemn we niet")
            ask(hoeveelbolletjes)

    
        print("Hier is uw ",BofH," met",AantalB," bolletjes")
        space()
        wiljemeer = input('wil je meer bestellen')
        
        if wiljemeer == "ja":
            
            print(AantalB)
            
            meerbol = AantalB + meerbol
            AantalB = meerbol
            hoeveelbolletjes = int(input('hoeveel bolletjes '))

        

        elif wiljemeer == "nee":
            AantalB = meerbol + AantalB
            print(AantalB)
            print("Bedankt en tot ziens")
            bon = bonnetje(AantalB )
            print
            break


def BakjeOfHoorn(AantalB):
    HoornAantal = 0
    BakAantal = 0

    if int(AantalB) <4:
        space()
        print("wilt u uw ",int(AantalB)," bollettjes in een hoorntke of bakje")
        space()
        print("voor een hoorntje kies A.Voor een bakje kies B")
        space()
        HB = input('Typ A of B')

        if HB == "A" or HB == "a":
            HoornAantal + 1
            HB = "hoorntje"
            print("hier sijn je ",AantalB," in je ",HB)
        
        if HB == "B" or HB == "b":
            BakAantal + 1
            HB = "bakje"
            print("hier sijn je ",AantalB," in je ",HB)
        return HB,HoornAantal,BakAantal

def welkesmaak(AantalB):
    for i in range(AantalB):
        V = "vanille"
        C = "Chocolade"
        M = "munt"
        A = "Aardbei"
        print("kies een smaak we hebben de smaken Vannile, chocolade, munt en aardbei")
        keuzesmaak = input('typ de eerste letter van de smaak die je wilt hebbben') 
        if keuzesmaak == "V" or keuzesmaak == "v":
            print(V)
        elif keuzesmaak == "C" or keuzesmaak == "c":
            print(C)
        elif keuzesmaak  == "M" or keuzesmaak == "m":
            print(M)
        elif keuzesmaak == "A" or keuzesmaak == "a":
            print(A)
        else:
            print('die smaak ijs hebben we niet maak opnieuw een keuze')
            welkesmaak()

          


def bonnetje(HoornAantal,AantalB,BakAantal):
    global hoornprijs 
    global bakprijs
    global bolprijs
    print("[PAPI Gelatto]--------------------------------")
    space()
    print(AantalB,"x",bolprijs,"=", (bolprijs * AantalB))
    space()
    print(HoornAantal,"x",hoornprijs,"=",())



   

def space():
    print("")
    print("")
    print("")

def shop():
    start()
    space()
    ask()
    
shop()