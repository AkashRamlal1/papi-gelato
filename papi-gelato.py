def welcome():
    space()
    print("--------------------------------------------")
    space()
    print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
    space()
    print("--------------------------------------------")
    space()


def ask():
    
    
    hoeveelbolletjes = int(input('hoeveel bolletjes '))

    bolletjes = hoeveelbolletjes

    if hoeveelbolletjes < 9:

        BakOfHorn = ask2(bolletjes)
    
    

    elif hoeveelbolletjes > 8:
        print("zulke grote baken hebbemn we niet")

    
        ask()


    print("Hier is uw", BakOfHorn, "met", bolletjes, "bolletjes")

    WasDatAlles = input('wil je meer bestellen')
    if WasDatAlles == "ja ":
        ask()
    elif WasDatAlles == "nee":
        print("Bedankt en tot ziens")


def ask2(bolletjes):
    A = "bakje"
    HofB = "bakje"
    if int(bolletjes) < 4:
        print("wilt u uw", int(bolletjes),"bolletjes in een hoorntje of een bakje")
        HofB = input('typ A voor een hoorntje en B voor een bakje ')

        if HofB == "a":
            HofB = "hoorntje"

        elif HofB == "b":
            HofB = "bakje"
    return HofB

        





def space():
    print("")
    print("")
    print("")

def shop():
    welcome()
    space()
    ask()
    


shop()