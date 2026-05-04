my_dictionary = {
    "aardbei" : "3",
    "vanille" : "4",
    "chocolade" : "5"
}
aanbieding = float(my_dictionary["vanille"]) * 0.8

reclame_tekst = (f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts €{aanbieding:.2f}")

#1.4
#print(reclame_tekst)

#1.5 heb ik anders opgelost, namelijk in 1.4 (het internet gebruikt voordat ik verder las)
#Ik snap ook niet helemaal hoe de uitkomst van 2.4000000000000000 er uit zou moeten zien. 
#Ik kreeg namelijk een foutmelding dat ik een float nodig had waardoor de uitkomst 3.2 werd, vervolgens laten tonen met 2 decimalen.

#1.6
reclame_tekst3 = reclame_tekst.upper()
#print(reclame_tekst3)

#1.7
reclame_tekst4 = reclame_tekst3.split()
#print(reclame_tekst4)

#1.8
# for el in reclame_tekst4:
#     print(el)

#1.9
# for el in reclame_tekst4:
#     print(el.lower())

#1.10
for el in reclame_tekst4:
    if len(el) <= 4:
       print(el.lower())
    if len(el) >= 5:
      print(el)
#Kreeg ik niet voor elkaar zonder wat hulp van het internet. heeft me 30 minuten geduurd voor ik doorhad dat ik el(len) i.p.v. len(el) aan het proberen was.
