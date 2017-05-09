print("Hej och välkommen till Paulines JULSTÄMNINGSMÄTARE! :)   ⛄")

print(" ")
print("Nu skall vi testa hur mycket julkänsla du har i år.")
print("Du svarar genom att skiva ditt svar efter frågan. Använd bara små bokstäver \ntack. När du har skrivit ditt svar, tryck enter.")


print(" ")
print("Om du är redo för första frågan, tryck enter")
input()
x1 = 0
a = input("1. Har du frivilligt spelat någon julmusik i år? ")
if a == "ja":
    x1 += 1
if a == "nej":
    x1 += 0

print(" ")

x2 = x1
a = input("2. Vem var julvärd förra året? Skriv bara förnamn. ")
if a == "gina":
    x2 += 1
if a == "Gina":
    x2 += 1
    print("Det stod där uppe att du bara får använda stor bokstav, men ok \nför den här gången.")
if a == "jina":
    x2 += 1
    print("Du stavade fel, men ok jag fattar vem du menar!")
if a == "Jina":
    x2 += 1
    print("Du stavade fel, men ok jag fattar vem du menar!")
else: 
    x2 += 0

print(" ")

x3 = x2
a = input("3. Vad äter du helst: sill eller päron? ")
if a == "sill":
    x3 += 1
else: 
    x3 += 0
    print("                                     Usch")

print(" ")

x4 = x3
a = input('4. Vilket är nästa ord i julsången: \nDet strålar en stjärna ... ')
if a == "förunderligt":
    x4 += 2
else: 
    x4 += 0

print(" ")

x5 = x4
while True:
    try:
        a = int(input('5. Hur många avsnitt av årets julkalender har du sett? '))  # OBS int()
        if a == 0 :
            x5 += 0
        if a in range(1,6):                     # in range för att testa mot mult values
            x5 += 1
        if a in range(6,11):
            x5 += 2
        if a in range(11,23):
            x5 += 3
        if a >= 23:
            x5 += 4
        else:
            x5 += 0
        break
    except ValueError:
        print("Använd siffror, inte bokstäver.")


print(" ")

x6 = x5
a = input("6. Har du ätit dopp i grytan idag? ")
if a == "ja":
    x6 += 1
if a == "nej":
    x6 += 0

print(" ")

x7 = x6
a = input("7. Har du just nu på dig något rött? ")
if a == "ja":
    x7 += 2
if a == "nej":
    x7 += 0

print(" ")

x8 = x7
a = input("8. Har du varit snäll i år? ")
if a == "ja":
    x8 += 2
if a == "nej":
    x8 += 0
else:
    x8 += 0

print(" ")

x9 = x8
a = input("9. Äter du senap till skinkan? ")
if a == "ja":
    x9 += 1
if a == "nej":
    x9 += 0

print(" ")

x10 = x9
a = input("10. Är det snö ute? ")
if a == "ja":
    x10 += 2
if a == "nej":
    x10 += 0

print(" ")

x11 = x10
a = input("Sista frågan med chans att vinna BONUSPOÄNG! Tycker du att jag har gjort ett bra quiz? ")
if a == "ja":
    x11 += 1
if a == "nej":
    x11 += 0

print(" ")
print(" ")
print("DITT JULSTÄMNINGSBETYG:")
print(" ")
if x11 in range(0,6):
    print("Åhhnej. Du har lika mycket julstämning som en midsommarstång. Du fick bara",x11,"av 18 poäng. \nDu behöver nog gå och ta dig en lussebulle.")
if x11 in range(6,9):
    print("Staffan var en Stalledräng, men du har inte så många poäng. Bara",x11,"av 18.")
if x11 in range(9,12):
    print("Du behöver kanske lite extra kristyr på pepparkakan, men ganska bra julstämning \n",x11,"av 18 poäng")
if x11 in range(12,15):
    print("Gläns över sjö och strand, du rodde",x11,"av 18 poäng i land. Bra julstämning!")
if x11 in range(15,18):
    print("Kanske är det du som skall vara tomte i år -",x11,"av 18 stämningsfulla poäng!")
if x11 >= 18:
          print("Rudolf är röd om mulen, du personifierar julen.",x11,"är maxpoäng!")

          
