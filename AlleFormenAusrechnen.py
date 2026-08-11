# Imports (bis jetzt Time & Mathe)
import time
import math


# Loop
Spielen = True
while Spielen == True:

# Einleitung mit Name und Form Auswahl
  Name = str(input("Wie heißt du?:"))
  Pi = float(3.141)
  Formen = "Zylinder; Kegel; Pyramide"
  time.sleep(0.7)
  print(f"Hallo {Name}")
  time.sleep(1)
  print("Wir werden gemeinsam jegliche Formeln ausrechnen aus verschiedensten Formen")
  time.sleep(1)
  Form = input(str("Mit welcher Form sollen wir heute anfangen?:" \
  f"     Verfügbar sind: {Formen}"))
  time.sleep(1)
  
# Zylinder mit Volumen und Oberflächeninhalt
  if Form == "Zylinder":
    Task = input(str("Wollen wir heute den Oberflächeninhalt oder das Volumen eines Zylinders berechnen?"))
    Einheit = str(input("Mit welcher Einheit rechnen wir heute?:"))
    if Task == "Oberflächeninhalt":

      
      time.sleep(0.67)
      R = float(input("Was ist der Radius deines Zylinders: "))
      time.sleep(1)
      H = float(input(("Was ist die Höhe deines Zylinders: ")))
      O = 2 * Pi * R * R + 2 * Pi * R * H
      print(f"Dein Oberflächeninhalt ist {O}{Einheit}²")
      time.sleep(1)
      Antwort = input(str("Willst du nochmal rechnen?(Ja/Nein)"))
      if Antwort == "Ja":
         Spielen = True
      else:
         Spielen = False
         print("Danke fürs benutzen - Made by Varto")
    if Task == "Volumen":
      R = float(input("Was ist der Radius deines Zylinders: "))
      time.sleep(1)
      H = float(input(("Was ist die Höhe deines Zylinders: ")))
      V = Pi * R * R * H 
      print(f"Das Volumen deines Zylinders beträgt{V}{Einheit}³")
      time.sleep(3)
      Antwort = input(str("Willst du nochmal rechnen?(Ja/Nein)"))
      if Antwort == "Ja":
         Spielen = True
      else:
         Spielen = False
         print("Danke fürs benutzen - Made by Varto")

# Wenn der Spieler Kegel gewählt hat O (Mit auslassung von H bzw. HS)
  if Form == "Kegel":
   Task1 = input(str("Wollen wir heute den Oberflächeninhalt oder das Volumen eines Kegels berechnen?"))
   time.sleep(1)
   Einheit1 = input(str("Mit welcher Einheit rechnen wir heute?:"))
   if Task1 == "Oberflächeninhalt":
      Bestätigung = input(str("Ist die Seitenhöhe gegeben(Ja/Nein)"))
      time.sleep(2)
      if Bestätigung == "Nein":
         R = float(input("Was ist der Radius deines Kegels: "))
         time.sleep(1)
         H = float(input("Was ist die Höhe deines Kegels?:"))
         O = Pi * R * R + Pi * R * (R * R + H * H)** 0.5
         time.sleep(2)
         print(f"Der Oberflächeninhalt deines Kegels beträgt: {O}{Einheit1}²")
         Antwort = input(str("Willst du nochmal rechnen?(Ja/Nein)"))
         if Antwort == "Ja":
           Spielen = True
         else:
           Spielen = False
           print("Danke fürs benutzen - Made by Varto")
      if Bestätigung == "Ja":
         R = float(input("Was ist der Radius deines Kegels: "))
         time.sleep(1)
         HS = float(input(("Was ist die Seitenhöhe deines Kegels(): ")))
         O = Pi * R * R + Pi * R * HS
         time.sleep(2)
         print(f"Der Oberflächeninhalt deines Kegels beträgt:{O}{Einheit1}²")
         Antwort = input(str("Willst du nochmal rechnen?(Ja/Nein)"))
         if Antwort == "Ja":
           Spielen = True
         else:
           Spielen = False
           print("Danke fürs benutzen - Made by Varto")
   # Volumen ausgewählt für Kegel (Mit ausslassung von H bzw. HS)
   if Task1 == "Volumen":
      Bestätigung1 = input(str("Ist H gegeben?(Ja/Nein):"))
      if Bestätigung1 == "Ja" or "ja":
         time.sleep(1)
         R = float(input("Was ist der Radius deines Kegels: "))
         time.sleep(1)
         H = float(input("Jetzt da wir wissen was H ist, sag es mir?"))
         time.sleep(0.3)
         V = 1/3 * Pi * H * R * R
         print(f"Dein Volumen beträgt {V}{Einheit1}³")
         Antwort = input(str("Willst du nochmal rechnen?(Ja/Nein)"))
         if Antwort == "Ja" or "ja":
           Spielen = True
         else:
           Spielen = False
           print("Danke fürs benutzen - Made by Varto")
      if Bestätigung1 == "Nein":
         R = float(input("Was ist der Radius deines Kegels: "))
         time.sleep(1)
         HS = float(input("Gib mir die Seitenhöhe, schnell!"))
         V = 1/3 * Pi * R * R * (HS * HS - R * R)** 0,5
         time.sleep(1)
         print(float(f"Das Volumen deines Kegels beträgt {V}{Einheit1}³"))
         Antwort = input(str("Willst du nochmal rechnen?(Ja/Nein)"))
         if Antwort == "Ja":
           Spielen = True
         else:
           Spielen = False
           print("Danke fürs benutzen - Made by Varto")
  # Pyramide ausrechnen
  if Form == "Pyramide":
    Task2 = input(str("Oberflächeninhalt oder Volumen(eif. O oder V eintippen)"))
    Einheit2 = input(str("Mit welcher Einheit rechnen wir heute?:"))
    if Task2 == "O":
      time.sleep(2)
      A = float(input("Was ist A deiner Pyramide?"))
      time.sleep(1)
      Bestätigung2 = input(str("Haben wir die Seitenhöhe oder müssen wir es berechnen?(Ja/Nein)"))
      time.sleep(1)
      if Bestätigung2 == "Ja" or "ja":
        HS = float(input("Gib mir die Seitenhöhe!"))
        O3 = A * A + 2 * A * HS
        time.sleep(2.3)
        print(f"Oberflächeninhalt deiner Pyramide ist:{O3}{Einheit2}²")
        time.sleep(1)
        Antwort = input(str("Willst du nochmal rechnen?(Ja/Nein)"))
        if Antwort == "Ja" or "ja":
          Spielen = True
        if Antwort == "Nein" or "nein":
          Spielen = False
          print("Danke fürs benutzen - Made by Varto")
      # Wenn Seitenhöhe nicht gegeben ist (O & Pyramide)
      if Bestätigung2 == "Nein" or "nein":
        H = float(input("Was ist die Höhe deiner Pyramide?:"))
        O4 = A * A + int(2) * A * (H * H + A/2 * A/2)** 0,5
        time.sleep(1)
        print(f"Dein Oberflächeninhalt ist da! : {O4}{Einheit2}²")
    # Volumen der Pyramide mit und ohne Seitenhöhe
    if Task2 == "V":
      Bestätigung3 = str(input("Ist die Seitenhöhe gegeben?:"))
      if Bestätigung3 == "Ja" or "ja":
        A = float(input("Was ist A deiner Pyramide?"))
        time.sleep(1)
        HS = float(input("Gib mir die Seitenhöhe!"))
        V1 = 1/3 * A * A * (HS * HS - A/2 * A/2)
        print(f"Das Volumen beträgt{V1}{Einheit2}³")
        Antwort = str(input("Willst du nochmal rechnen?(Ja/Nein)"))
        if Antwort == "Ja" or "ja":
          Spielen = True
        else:
          Spielen = False
          print("Danke fürs benutzen - Made by Varto")
      if Bestätigung3 == "Nein" or "nein":
        G = float(input("Was ist die Grundfläche deiner Pyramide?"))
        time.sleep(1)
        H = float(input("Was ist die Höhe deiner Pyramide?"))
        V2 = 1/3 * G * H 
        print(f"Das Volumen deiner Pyramide beträgt{V2}{Einheit2}³")
        Antwort = input(str("Willst du nochmal rechnen?(Ja/Nein)"))
        if Antwort == "Ja" or "ja":
          Spielen = True
        if Antwort == "Nein" or "nein":
          Spielen = False
          print("Danke fürs benutzen - Made by Varto")

        

















      
 
         
       
   



              