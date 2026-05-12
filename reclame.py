from algemene_functies import mijn_functie_2

#Vraag 8.4 en 8.5

def aanbieding_1(smaak, prijs, korting):
    return (f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs-korting*prijs:.2f}")

#test_functie_aanbieding_1 = aanbieding_1("aardbei", 4, 0.1)
#print(test_functie_aanbieding_1)

#Vraag 8.6 en 8.7

def inkomsten_totaal(inkomsten, btw):
    print(f"Het totaal van alle inkomsten van deze week is {sum(inkomsten)} euro, waarover {sum(inkomsten)*btw} euro btw betaald dient te worden.")
    
inkomsten = [220, 430, 125, 160, 205, 90, 345]
btw = 0.09 

#inkomsten_totaal(inkomsten, btw)


#Vraag 8.8

def laag_en_hoog(mijn_lijst):
    return max(mijn_lijst), min(mijn_lijst)

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]

#print(laag_en_hoog(mijn_lijst))

#Vraag 8.9 en 8.10

def gemiddelde(mijn_lijst):
    tekst = f"De gemiddelde inkomsten deze week zijn {sum(mijn_lijst) / len(mijn_lijst)} euro."
    return tekst

#print(gemiddelde(mijn_lijst))

#Vraag 8.11

def meervoudig(invoer_lijst):
    return(laag_en_hoog(invoer_lijst))

invoer_lijst = [10,5,3,2,1,2,9]
#print(meervoudig(invoer_lijst))
    
#Vraag 8.12

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0] , korte_lijst[1])

invoer_lijst2 = [3,5]
#print (combinatie(invoer_lijst2))
