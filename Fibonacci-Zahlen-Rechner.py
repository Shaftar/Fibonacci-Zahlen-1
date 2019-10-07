"""Fibonacci Zahlem Rechner
   Autor: Mohamad Shaftar
   Datum: 25.09.2019
   """
f0 = 0  # Der alte Wert speichern
f1 = 1  # passt dem neuen wie alten wert ein
f2 = 1  # Der neue Wert speichern
zahl = int(input('Enter the number of output:'))
while zahl <= 0:  # Eingabe überprüfen
    zahl = int(input('Bitte geben Sie positive Zahlen ein:'))  # Erneut Eingabe
    continue  # Wenn die bedienung wahr ist, soll weiter laufen
else:  # Beginn der Berechnung
    for i in range(zahl):  # Iteratives Verfahren
        i += 1  # Um genau Laüfe der Schleife zu bestimmen
        print(f0)   # Ausgabe
        f0 = f1  # Erste Zahl
        f1 = f2  # Zweite Zahl
        f2 = f1 + f0  # Der neue Wert
