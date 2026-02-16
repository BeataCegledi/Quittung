name = input("Hallo! gib mir dein Name: ")
print("Willkommen ",name,"!")
running = True
while running: 
    while True:
        try: 
            budget = int(input("\nWie groß ist dein Budget (€)? "))
            break
        except ValueError:
            print("Bitte nur Zahlen eingeben!")
            continue
    print("\n------------------------------------\n")

    #  einlesen_drei_artikel mit dictionary
    while True:    
        artikel_dict = {}
        zwischensumme = 0.0
        for i in range (1,4,1):
            artikel_dict[i] = {}
            print(i,". Artikel: \n")
            
            artikel_dict[i]["name"] = input("Gib mir erstmal den Artikelname: ")

            while True:
                try: 
                    artikel_dict[i]["preis"] = round(float(input("Wieviel kostet ein Stück (€)? ").replace(",", ".")),2)
                    if artikel_dict[i]["preis"] >=0:
                        break
                    print("Preis kann nur positive Zahl sein!")
                except ValueError:
                    print("Bitte nur Zahlen eingeben! (Das Programm rechnet nur mit max 2 Kommazahlen)")
                    continue
        
            while True:
                try: 
                    artikel_dict[i]["menge"] = int(input("Wieviel Stück möchtest du kaufen? "))
                    if artikel_dict[i]["menge"] >=0:
                        break
                    print("Bitte nur positive Zahl eingeben!")
                except ValueError:
                    print("Bitte nur ganze Zahl eingeben!")
                    continue
  
            print("\nHinzugefügt: ",artikel_dict[i]["name"],": ",artikel_dict[i]["preis"],"€ * ",artikel_dict[i]["menge"]," = ",artikel_dict[i]["preis"]*artikel_dict[i]["menge"])
            print(" ")
            zwischensumme += (artikel_dict[i]["preis"]*artikel_dict[i]["menge"])
            print("Zwischensumme: ",zwischensumme)
        print("\n----------------------------------\n")
        print("0: Kein Rabatt")
        print("1: Student - 10% Rabatt")
        print("2: VIP-Kunde - 15% Rabatt")
        print("3: Gutschein 5€ - Nur ab einen Einkaufswert von 20€ einlösbar!")
        print(" ")
        while True:
            try:    
                rabatt = int(input("Hast du ein Rabatt oder einen Gutschein? "))
                if rabatt <0 or  rabatt >3:
                    print("Bitte nur einen Zahl zwischen 0 und 3 eingeben!")
                else:
                    break 
            except ValueError:
                print("Bitte nur ganze Zahl eingeben!")
#Rabatt       
        print("\n------------------------------------\n")
       
        if rabatt == 0:
            summe = zwischensumme
            rabtext = "Kein Rabatt"
            rabsum = 0
            print(rabtext)
        elif rabatt == 1:
            summe = zwischensumme*0.9
            rabtext = "Student -10%"
            rabsum = -zwischensumme*0.1
            print(rabtext,": ",rabsum)
        elif rabatt == 2:
            summe = zwischensumme*0.85
            rabtext = "VIP -15%"
            rabsum = -zwischensumme*0.15
            print(rabtext, ": ",rabsum)
        else:
            if zwischensumme<20:
                print("Einen Gutschein kannst du erst ab 20€ Einkaufssumme einlösen! Vieleicht beim nächtesn Einkauf")
            else:
                summe = zwischensumme-5
                rabtext = "Gutschein 5€"
                rabsum = -5
                print(rabtext)
       
        print("\n------------------------------------\n")
        print("Zu Zahlen ist",round(summe,2))     
        print("\n------------------------------------\n")
        break
    #Quittung
    print("\n"*6,"***************************** QUITTUNG **********************************\n")
    print("Kunde: ",name)
    print("\nArtikel: \n")
    for i in range (1,4,1):
#      print(i,": ",artikel_dict[i]["name"],artikel_dict[i]["preis"],"€ x ",artikel_dict[i]["menge"]," = ",artikel_dict[i]["preis"]*artikel_dict[i]["menge"],"€")
        print(f"{i}. {artikel_dict[i]['name']:.<40}{artikel_dict[i]['preis']:>6.2f} € x {artikel_dict[i]['menge']:>4} = {artikel_dict[i]['preis']*artikel_dict[i]['menge']:>8.2f} €")
    print("\n=========================================================================\n")
    print(f"\nZwischensumme:{zwischensumme:>55.2f} €")
    print(f"\nRabatt ({rabtext}):{rabsum:>51.2f} €")
    print(f"\nEndsumme:{summe:>60.2f} €")
    print(f"\nBudget:{budget:>64.2f} €")
    budget -= summe
    if budget >= 0:
        print(f"\n\nRestbudget:\t{budget:>54.2f} €\nStatus:     OK ☺")
    else:
        print("\n\nStatus:   Du hast leider nicht genug Geld!")
    

    while True:
        print("\n*************************************************************************\n")
        again = input("\nMöchtest du nochmal einkaufen (j/n?").lower()
        if again == "n":
            print("\n\n------------------------------------\n")
            print("Wir freuen uns auf dich nächstes mal wieder!")
            print("\n------------------------------------\n")
            running = False
            break
        elif again == "j":
            break
        else:
            print("\nBitte nur j oder n eingeben!")

   
