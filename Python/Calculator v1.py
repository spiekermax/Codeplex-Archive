#Einfacher Taschenrechner
print ("(c) Maximilian Spiekermann, 2016")

#Hauptfunktion
def main ():
    #Anwender kann Text eingeben
    userinput = input ("")
    if (userinput == ""):
        print ("Bitte gebe etwas ein!")
        main ()
    else:
    #Ersetze ungültige Operatoren
        userinput = userinput.replace (':', '/')
        userinput = userinput.replace (',', '.')
        userinput = userinput.replace ('^', '**')
        userinput = userinput.replace ('=', '==')

        #Versuche die Eingabe auszuwerten
        try:
            #Werte aus
            resultAsInt = eval (userinput)
            #Konvertiere Ergebnis zu einer Variable des Typen 'String'
            resultAsStr = str(resultAsInt)
            #Übersetze output
            resultAsStr = resultAsStr.replace('True', 'Das ist wahr.')
            resultAsStr = resultAsStr.replace('False', 'Das ist falsch.')
            #Zeige das Ergebnis an
            print (resultAsStr)
        #Falls die Eingabe ungültig ist
        except NameError:
            print ("Bitte benutze keine ungültigen Buchstaben!")
        except SyntaxError:
            print ("Bitte benutze nur gültige Operatoren!")
        except ZeroDivisionError:
            print ("Du kannst nicht durch '0' teilen!")
        #Im Falle eines anderen Fehlers
        finally:
            pass
        #Wiederhole die Funktion        
        main ()

#Führe main() das erste mal aus    
try:
    main ()
#Im Falle eines unbekannten Fehlers
finally:
    print ("Ein Fehler ist aufgetreten. Bitte versuchen Sie es erneut.\n")
    main ()
