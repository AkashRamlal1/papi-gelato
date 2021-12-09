ijsprijs = 1.1
hoornprijs = 1.25
bakprijs = 0.75


def space():
    print('')
    print('')

def welkom():
    space()
    print('-----------------------------------------------')
    space()
    print("welkom bij papi gelato")
    space()
    print('-----------------------------------------------')
    space()

def start():
    welkom()
    HoornAantal = 0
    BakAantal = 0

    bol = int(input('hoeveel ijs wil je')) #vraagt het aantal gewentste bolletjes
    bolletjes = bol

    space()
    print(" je wilt ",bolletjes," bollen ijs")
    while bolletjes > 0:
        
        if bolletjes < 9:
            smaak = welkesmaak(bolletjes)
            BofH = BakjeOfHoorn(bolletjes)
                                                                                                                                                                                                                                                                                                                                                    
        elif bol > 8:
            print("zulke grote baken hebbemn we niet")
            start(bol)

        print("Hier is uw ",BofH," met",bolletjes," bolletjes")
        space()
        wiljemeer = input('wil je meer bestellen')
        meerbol = 0
         
        
        if wiljemeer == "ja":
            
            print(bolletjes)
            extrabol = int(input('hoeveel bolletjes wil je'))
            print(extrabol)
            meerbol = extrabol
            print(meerbol + bolletjes)


       
            
            

        

        elif wiljemeer == "nee":
             
            bolletjes = meerbol + bolletjes
            print(bolletjes)
            print("Bedankt en tot ziens")
            bon(bolletjes,HoornAantal,BakAantal,BofH)
            
            break


def welkesmaak(bolletjes):
    for i in range(bolletjes):
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

            



def BakjeOfHoorn(AantalB):
    

    if int(AantalB) <4:
        space()
        print("wilt u uw ",int(AantalB)," bollettjes in een hoorntke of bakje")
        space()
        print("voor een hoorntje kies A.Voor een bakje kies B")
        space()
        HB = input('Typ A of B')

        if HB == "A" or HB == "a":
            HB = "hoorntje"
            print("hier sijn je ",AantalB," in je ",HB)
        
        if HB == "B" or HB == "b":

            HB = "bakje"
            print("hier sijn je ",AantalB," in je ",HB)
        return HB

def bon(bolletjes,Hoornaantal,Bakaantal,BofH):
    
    global ijsprijs
    global hoornprijs
    global bakprijs
    boltotaal = bolletjes * ijsprijs
    hoornttotaal = Hoornaantal * hoornprijs
    baktotaal = Bakaantal * bakprijs
    

    
    space()
    print('--[papi gelato]-------------------')
    space()
    print('je bestelling')
    space()
    print(bolletjes,"x"," bolletjes ijs         ",boltotaal)
    space()
    print(Hoornaantal,"x"," bolletjes ijs         ",hoornttotaal)
    space()
    print(Bakaantal,"x"," bolletjes ijs         ",baktotaal)


def shop():
    start()
    

shop()
