#Variablen Import
import random
from os import system, name
import time
import sqlite3
import keyboard

rechenoperatoren = ["+", "-", "*", "/"]
eingabe_schwierigkeit = "1"
eingabe_runden = "1"
rechenstandart = "1"
richtige_aufgaben = 0
aufgabe_durchgefuehrt = 0

def optionen():
    global eingabe_schwierigkeit, eingabe_runden, rechenstandart
    print("+--------+\n|Optionen|\n+--------+")
    eingabe = input("Einstellungen wählen:\n[1]: Schwierigkeit\n[2]: Runden Loop\n[3]: Rechenzeichen\n> ")
    try:
        int(eingabe)
    except ValueError:
        print(f"'{eingabe}' ist keine gültige Option!")
        time.sleep(0.8)
        clear()
        optionen()
    if eingabe == "1":
        clear()
        print("Schwierigkeiten:\n1: Beide Operanden einstellig z. B. 5 * 6\n2: Erster Operand zweistellig, zweiter Operand einstellig z. B. 56 – 7\n3: Beide Operanden zweistellig z. B. z. B. 34 * 56\n4: Erster Operand dreistellig, zweiter Operand zweistellig 123 – 56")
        eingabe_schwierigkeit = input("> ")
        try:
            int(eingabe_schwierigkeit)
        except ValueError:
            print("Bitte gib eine ganze Zahl ein!")
            time.sleep(0.8)
            clear()
            optionen()
    if eingabe == "2":
        clear()
        print("Runden Loop:\nWie viele Aufgaben willst du auf einmal rechnen?")
        eingabe_runden = input("> ")
        try:
            int(eingabe_runden)
        except ValueError:
            print("Bitte gib eine ganze Zahl ein!")
            time.sleep(0.8)
            clear()
            optionen()
    if eingabe == "3":
        clear()
        print("Rechenoperator wählen:\n[1]: Shuffle\n[2]: Addition\n[3]: Subtraktion\n[4]: Multiplikation\n[5]: Division")
        rechenstandart = input("> ")
        try:
            int(eingabe_runden)
        except ValueError:
            print("Bitte gib eine ganze Zahl ein!")
            time.sleep(0.8)
            clear()
            optionen()
    main()
#Main Methode die beim Start des Programmes ausgeführt wird
def main():
    clear()
    print("Willkommen zum Training\n***********************")
    eingabe = input("Wähle eine Option:\n[1]: Rechnen\n[2]: Ergebnis\n[3]: Optionen\n> ")
    try:
        int(eingabe)
    except ValueError:
        print(f"'{eingabe}' ist keine gültige Option!")
        time.sleep(0.8)
        clear()
        main()
    if eingabe in ("1", "rechnen", "Rechnen"):
        clear()
        rechnen()
    elif eingabe in ("2", "ergebnis", "Ergebnis"):
        clear()
        ergebnis()
    elif eingabe  in ("3", "optionen", "Optionen"):
        clear()
        optionen()
#Methode um die Konsole zu clearen
def clear():
    if name == 'nt':
        _ = system('cls')

#Methode um das Ergebnis auszuwerten und anzuzeigen
def ergebnis():
    global richtige_aufgaben, aufgabe_durchgefuehrt
    if aufgabe_durchgefuehrt == 0:
        print("Bitte rechne erst ein paar Aufgaben.")
        time.sleep(0.8)
        clear()
        main()
    else:
        print("+--------+\n|Ergebnis|\n+--------+")
        print(f"Insgesamt:  {aufgabe_durchgefuehrt}")
        print(f"Richtig:    {richtige_aufgaben}")
        proz_richtig = 100*richtige_aufgaben/aufgabe_durchgefuehrt
        print(f"Prozentual: {proz_richtig}%\n\n")
        print("Press 'esc' to exit.")
        if keyboard.read_key() == "esc":
            main()   
#Methode zur Erzeugung von Rechnungen
def rechnen():
    global eingabe_schwierigkeit,eingabe_runden, richtige_aufgaben, aufgabe_durchgefuehrt
    print("+-------+\n|Rechnen|\n+-------+")
    eingabe_runden_int = int(eingabe_runden)
    for aufgabe in range(eingabe_runden_int):
        if eingabe_schwierigkeit == "1":
            erste_zahl1 = 1
            zweite_zahl1 = 9
            erste_zahl2 = 1
            zweite_zahl2 = 9
        if eingabe_schwierigkeit == "2":
            erste_zahl1 = 10
            zweite_zahl1 = 99
            erste_zahl2 = 1
            zweite_zahl2 = 9
        if eingabe_schwierigkeit == "3":
            erste_zahl1 = 10
            zweite_zahl1 = 99
            erste_zahl2 = 10
            zweite_zahl2 = 99
        if eingabe_schwierigkeit == "4":
            erste_zahl1 = 100
            zweite_zahl1 = 999
            erste_zahl2 = 10
            zweite_zahl2 = 99
        if rechenstandart == "1":
            operator = random.choice(rechenoperatoren)
        if rechenstandart == "2":
            operator = "+"
        if rechenstandart == "3":
            operator = "-"
        if rechenstandart == "4":
            operator = "*"
        if rechenstandart == "5":
            operator = "/"
        number1 = random.randint(erste_zahl1,zweite_zahl1)
        number2 = random.randint(erste_zahl2,zweite_zahl2)
        print(number1,operator,number2)
        if operator == "+":
            ergebnis_loesung = number1+number2
        if operator == "-":
            ergebnis_loesung = number1-number2
        if operator == "*":
            ergebnis_loesung = number1*number2
        if operator == "/":
            ergebnis_loesung_old = number1/number2
            ergebnis_loesung = round(ergebnis_loesung_old, 2)      
        ergebnis_eingabe = input("Gebe das Ergebniss ein:\n> ")
        try:
            ergebnis_loesung_conv = float(ergebnis_loesung)
            ergebnis_eingabe_conv = float(ergebnis_eingabe)        
            if ergebnis_loesung_conv == ergebnis_eingabe_conv:
                clear()
                print(f"Aufgabe {aufgabe+1}/{eingabe_runden}")
                print("Super gemacht!\n\n\n\n")
                richtige_aufgaben += 1
                time.sleep(0.6)
                clear()
        except ValueError:
            pass
        aufgabe_durchgefuehrt += 1
    main()

main()