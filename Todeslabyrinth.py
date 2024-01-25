import time
import sys





print("Herzlich willkommen im Todeslabyrinth")
time.sleep(1)
print("Im Spiel geht es um,")
time.sleep(1)
print("Leben")
time.sleep(1)
print("und")
time.sleep(1)
print("Tod")
time.sleep(2)
print("Regeln:")
time.sleep(1)
print("Du durchläufst das Labyrinth mit 3 Leben.")
time.sleep(2)
print("Wähle die für dich klügste Entscheidung aus.")
time.sleep(2)
print("Wenn deine Leben aufgebraucht sind, bist du TOT")
time.sleep(2)
print("Ziel:")
time.sleep(2)
print("ÜBERLEBEN")
time.sleep(1)


frage=input("Verstanden?\n(Ja/Nein)")
if frage.lower()== "ja":
    time.sleep(1)
    print("Gut")
    time.sleep(1)
    print("Los geht's")
    time.sleep(1)
else:
    print("Angsthase!")
    time.sleep(2)
    sys.exit()



print("Du wachst eines Morgens auf und merkst, dass du nicht zu Hause bist.")
time.sleep(1)
print("Du bist im ...")
time.sleep(2)
print("TODESLABYRINTH")
time.sleep(1)


def Runde1(live):
    Antwort= ""
    Loop_fortsetzen=True

    while Loop_fortsetzen:
     print("Stehst du auf...")
     time.sleep(1)
     print("... oder, bleibst du liegen und hoffst, es ist nur ein Traum?")
     time.sleep(2)
     print("1=Aufstehen \n2=Liegen bleiben")
     Antwort = input()
     time.sleep(2)

     if Antwort == "1":
         print("Gute Entscheidung...")
         time.sleep(2)
         Loop_fortsetzen=False


     elif Antwort == "2":
         live -= 1
         print("Schade, ein Bär weckt dich und wirst beim kampf verletzt.\nDu überlebst mit einem Leben weniger")
         time.sleep(3)
         print("Dein Leben beträgt: ", live)
         time.sleep(3)
         Loop_fortsetzen=False

     else:
         print("Bist du blöd?? Gib 1 oder 2 ein!!")
         Loop_fortsetzen=True


    return Antwort, live




def Runde2(Antwort, live):
    Loop_fortsetzen=True

    while Loop_fortsetzen:
     print("Es geht weiter ...")
     time.sleep(1)
     if Antwort == "2":
      print("Der Bär ist weg")
     time.sleep(1)
     print("Du gehst eine Weile und siehst einen Baum")
     time.sleep(1)
     print("Du hast Hunger...")
     time.sleep(1)
     print("... und du siehst einen roten Apfel")
     time.sleep(1)
     print("Isst du den?")
     time.sleep(1)
     print("Ja oder Nein?")
     Antwort2=input("")

     if Antwort2.lower() =="ja":
         print("Puuh")
         time.sleep(1)
         print("Glück gehabt")
         time.sleep(1)
         print("Der Apfel ist lecker")
         time.sleep(2)
         Loop_fortsetzen=False
     elif Antwort2.lower() == "nein":
         live -= 1
         time.sleep(1)
         print("Du hast Hunger !!!!")
         time.sleep(1)
         print("Dein Leben beträgt: ", live)
         time.sleep(2)
         Loop_fortsetzen=False
     else:
         print("Was soll das??")
         time.sleep(1)
         print("Gib 'JA' oder 'Nein' ein!!")
         time.sleep(1)
         Loop_fortsetzen=True



    return live





def Runde3(live):
    Antwort3=""
    Loop_fortsetzen = True





    while Loop_fortsetzen:
     print("Du suchst weiter verzweifelt nach einem Ausgang.")
     time.sleep(2)
     print("Ohh, da ist eine Katze...")
     time.sleep(1)
     print("Folgst du ihr?")
     time.sleep(1)
     Antwort3 = input("Ja oder Nein").lower()

     if Antwort3 == "ja":
         print("Ist sie gut oder Böse?")
         time.sleep(2)
         print("Wirst du es bereuern?")
         time.sleep(2)
         print("Sie geht in eine Waldhütte...")
         time.sleep(3)
         print("... und legt sich schlafen")
         time.sleep(3)
         print("Dort ist auch ein Bett und warmes Essen für dich.")
         time.sleep(3)
         print("Du übernachtest dort")
         time.sleep(1)
         Loop_fortsetzen=False
     elif Antwort3 == "nein":
         print("Du verbrinst die Nacht dort, wo du gerade bist.")
         time.sleep(3)
         print("ALLEIN")
         time.sleep(2)
         print("DRAUßEN")
         time.sleep(2)
         print("IM DUNKELN")
         time.sleep(2)
         print("ES IST KALT")
         time.sleep(1)
         print("!!!")
         live -= 1
         time.sleep(1)
         print("Dein Leben beträgt:", live)
         Loop_fortsetzen=False
     else:
         print("BIST DU BLÖD???")
         time.sleep(6)
         print("Gib JA oder NEIN ein")
         time.sleep(1)
         print(";)")
         time.sleep(1)
         Loop_fortsetzen=True


    return Antwort3, live


def Runde4(Antwort3, live):

    Loop_fortsetzen=True

    while Loop_fortsetzen:

        print("Guten Morgen")
        time.sleep(1)
        if Antwort3.lower == "nein":
            print("Naaa...")
            time.sleep(2)
            print("War es kalt?")
            time.sleep(2)
            print(";)")
            time.sleep(1)
        elif Antwort3.lower == "ja":
            print("Ich hoffe, du hast gut und lange geschlafen.")
            time.sleep(1)

        print("Du gehst eine Weile geradeaus ...")
        time.sleep(2)
        print("Nach einer Weile endet der Weg.")
        time.sleep(2)
        print("Da sind zwei Türen")
        time.sleep(2)
        print("Eine Blaue Tür ...")
        time.sleep(1)
        print("... eine Grüne Tür")
        time.sleep(3)
        print("Welche wählst du?")
        Antwort4=input("G=Grün \nB=Blau\n")

        if Antwort4.lower() == "g":
           print("Die Tür führt ...")
           time.sleep(2)
           print("... in den nächsten Gang")
           time.sleep(1)
           print("Schade")
           time.sleep(1)
           print("Deine geistigen Kräfte lassen langsam nach.")
           time.sleep(2)
           print("Du willst umkehren, ...")
           time.sleep(1)
           print("... aber die Türen sind weg.")
           time.sleep(1)
           print("Du bist verzweifelt")
           time.sleep(2)
           live -= 1
           print("Dein Leben beträgt:", live)
           time.sleep(2)
           Loop_fortsetzen=False
        elif Antwort4.lower() == "b":
            print("Juhu")
            time.sleep(1)
            print("Du bist im schönsten Stadion der Welt")
            time.sleep(2)
            print("Im...")
            time.sleep(2)
            print("VOLKSPARKSTADION")
            time.sleep(1)
            print("Herzlichen Glückwunsch")
            time.sleep(1)
            print("Du bist aus dem ...")
            time.sleep(1)
            print("TODESLABYRINTH")
            time.sleep(1)
            print("entkommen")
            time.sleep(1)
            input()
            sys.exit()
        else:
            print("Gib B oder G für Blau oder Grün ein!")
            Loop_fortsetzen=True

    return live





def finale_Runde():
    Loop_fortsetzen=True

    while Loop_fortsetzen:
     print("Herzlich Willkommen im Finale")
     time.sleep(2)
     print("Diese Runde entscheidet darüber, ob du frei kommst \n"
           "oder für immer im Todeslabyrinth bleibst.")
     time.sleep(4)
     print("Nachdem du durch die Tür gegangen bist, \n"
           "bist du einen Augenblick weitergegangen...")
     time.sleep(4)
     print("...bis es nur noch rechts und links lang geht")
     time.sleep(2)
     print("An der Wand vor dir steht:\n"
          "entscheide dich weise")
     time.sleep(2)
     print("Wählst du den richtigen Weg bist du frei")
     time.sleep(1)
     print("Wählst du den Falschen, bleibst du für immer im...")
     time.sleep(3)
     print("TODESLABYRINTH")
     time.sleep(1)
     frage=input("Gehhst du links oder rechts lang?\n(links/rechts)")
     time.sleep(1)

     if frage.lower()=="rechts":
         print("Du gehst eine Weile...")
         time.sleep(1)
         print("...es kommt nichts.")
         time.sleep(1)
         print("Du willst umdrehen...")
         time.sleep(2)
         print("Doch es ist zu spät ...")
         time.sleep(2)
         print("...hinter dir ist nichts mehr")
         time.sleep(2)
         print("Deshalb gehst du weiter ...")
         time.sleep(2)
         print("...nach einer Weile wird es heller")
         time.sleep(2)
         print("Hast du es geschafft?")
         time.sleep(5)
         print("JAAAA")
         time.sleep(1)
         print("Du kommst an einer Seitengasse in Hamburg raus...")
         time.sleep(1)
         print("Herzlichen Glückwunsch")
         time.sleep(3)
         print("Du bist frei")
         time.sleep(1)
         print(";)")
         time.sleep(1)
         input()
         sys.exit()
     elif frage.lower()=="links":
         print("Du gehst eine Weile...")
         time.sleep(1)
         print("...es kommt nichts.")
         time.sleep(1)
         print("Du willst umdrehen...")
         time.sleep(2)
         print("Doch es ist zu spät ...")
         time.sleep(2)
         print("...hinter dir ist nichts mehr")
         time.sleep(2)
         print("Deshalb gehst du weiter ...")
         time.sleep(2)
         print("...nach einer Weile wird es heller")
         time.sleep(2)
         print("Hast du es geschafft?")
         time.sleep(5)
         print("Nein")
         time.sleep(1)
         print("Leider nicht")
         time.sleep(3)
         print("Tut mir leid")
         time.sleep(2)
         print("Du bleibst für immer im Todeslabyrinth verloren")
         time.sleep(2)
         input()
         sys.exit()

     else:
         print("Links oder Rechts!")
         time.sleep(2)
         Loop_fortsetzen=True







HSV = 1
Beste_Mannschaft = 1






def game_over():
    print("Schade")
    time.sleep(2)
    print("Du bist Tod")
    time.sleep(2)
    if int(HSV) == int(Beste_Mannschaft):
        print("Vielleicht beim nächsten mal")
        input("")
        sys.exit()



def main():
    live=3

    antwort_Runde1, live = Runde1(live)
    live = Runde2(antwort_Runde1, live)
    antwort3_Runde3, live = (Runde3(live))


    if live == 0:
        game_over()
    else:
        live = Runde4(antwort3_Runde3, live)
    if live == 0:
        game_over()
    else:
        finale_Runde()










main()