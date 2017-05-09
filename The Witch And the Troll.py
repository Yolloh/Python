import random
import time
import random

global liv
global mat

liv = 5
mat = 4

def troll():
    mat += 2
    print("Du fick ost och blåbär av trollet")
    print("Din mat är",mat,", Ditt liv är",liv)

def haxa():
    liv -= 1
    mat -= 1
    print("Häxan åderlät dig!")
    print("Din mat är",mat,", Ditt liv är",liv)

def nacken():
    liv -= 2
    print("Näcken försökte dränka dig!!")
    print("Din mat är",mat,", Ditt liv är",liv)

def alvan():
    liv += 1
    print("""Älvan lovar guld och gröna skogar, men skenet bedrar när all kommer kring..
    Nåväl, hon höll ett vakande öga på dig medans du sov ut i den blöta björnmossan.""")
    print("Din mat är", mat, ", Ditt liv är", liv)

fiender = [alvan, troll, nacken]

            # Den kör alla fiender functioner direkt! Bara att ha dem i dict verkar call...
            # Mat och liv är alltid samma - borde ha dem i start func eller en karaktär.
            # Kanske göra karaktären till ett dictionary? Liv : 3, Mat : 4, Slag : 8

print(f"""Mellan stockar och stenar, mossor och bark
      en stig letar alltjämt sig fram
      Du kommer till en förgrening.
      Din mat är {mat}, ditt liv är {liv}
      Vart går du?""")
while liv >= 1:
  #  if liv <= 0 or mat <= 0:
  #      break
    direction = input("Höger, rakt eller vänster? ").lower()

    if direction == "höger":                    # Funkar inte, "liv" ref before assigment
        nacken()
    elif direction == "vänster":
        mat += 1
        print("Du möter tomten Hans. Han ger dig ett äpple.")
        print("Din mat är", mat, ", Ditt liv är", liv)
        print("Du kommer till en ny förgrening. Vart vill du gå: vänster eller rakt?")
        hansdirection = input("> ").lower()
        if hansdirection == "vänster":
            troll()
        else:
            random.choice(fiender)      # LISTA av fiender(functions) Blir ej callade.... Kanske ändåå inte går.
    elif direction == "rakt":
        print("""Den här vägen verkar... ändlös.
        Bäst att fortsätta gå, och raska på innan mörkret kommer. Låt oss hoppas du klarar dig..""")
        liv -= 2
        time.sleep(3)
        print("Din mat är", mat, ", Ditt liv är", liv)
        print("..fortsätt gå!...")
        time.sleep(5)
        print("""Du är försvagad, men klarade dig. Tillslut tätnar granarna bakom dig,
        och en ny korsning väntar i en dunge: """)
        nomansland = input("Höger eller vänster >")
        if nomansland == "vänster":
            print("""En ljus gestalt närmar sig sakta mellan trästammarna. Det är Älvan.
            Hon ser att du är trött och hungrig, och hennes ljuva stämma erbjuder dig att komma med henne,
            och låta henne bjuda dig på en stor middag med grillade vildsvin, och därefter en varm mjuk
            bädd att sova i.
            Vill du ta hennes erbjudande?""")
            alvansvag = input(">").lower()
            if alvansvag == "ja":
                alvan()
                if liv >= 0 or mat >= 0:
                    break
            else:
                print("Din mat är", mat, ", Ditt liv är", liv)
                continue                                                # continue funkar! yaya! :)
        elif nomansland == "höger":
            print("""Du korsar en liten bäck, och sätter dig på en sten. Du ser att det växer lite bär och svampar
            längst stigen. Vill du plocka och äta dem?""")
            bar = input("> ")
            if bar == "ja":
                mat += 1
                print("Det var gott med lite mat i magen. ")
                print("Din mat är", mat, ", Ditt liv är", liv)

            else:
                print("Hungrig fortsätter du din vandring")
                print("Din mat är", mat, ", Ditt liv är", liv)

    else:
        haxa()
        if liv >= 0 or mat >= 0:
            break
        else:
            continue
if mat <= 0:
    print("Du svalt ihjäl.. Sakta tynar din kropp bort bakom en rotvälta.")

if liv <= 0:
    print("Du dog.")

def start():
    road = (input("Vart vill du gå? "))
    if road == "Hem":
        print("Hejdå!")
    else:
        time.sleep(2)



"""
                if liv >= 0 or mat >= 0:
                    break
                else:
                    continue
"""












