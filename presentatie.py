
def presenteer(dictionary, totaal):
    for k, v in dictionary.items():
        print(f"{k} : {v} euro")
    print("==========================")
    print(f"totaal : {totaal} euro")
    
mijn_dict = {'vis' : 10, 'vlees': 25, 'overig' : 15}
totaal = 50

presenteer(mijn_dict, totaal)

#Ik weet dat ik beter niet kan printen in de functie maar ik kreeg dan of alleen de laatste of alleen de eerste itteratie van de loop bij return.
#Het vreemde is als ik even terugga naar les 6 dan werkt onderstaande voorbeeld uit de stof wel.
#Het lijkt dus de combinatie van functie, loop en dictionary te zijn waardoor ik maar 1 line van de dictionary te zijn krijg.




'''mijn_dictionary = {
    "Voornaam" : "Harry",
    "Geboortedatum" : "31-maart-1939",
    "Registratienummer" : "AA18891"
}
for k, v in mijn_dictionary.items():
    print (k, v)
'''
