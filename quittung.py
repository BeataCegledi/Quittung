# =============================================================================
# Quittung – Mini-Shop-Kasse
# Autor: Beata Cegledi
# Beschreibung: Konsolenprogramm fuer eine einfache Ladenkasse.
#               Der Nutzer gibt 3 Artikel ein, waehlt eine Rabattart
#               und bekommt eine formatierte Quittung mit Budgetkontrolle.
#
# Konzepte: while, for, try/except, if/elif/else, Dictionary, f-Strings
# =============================================================================

# --- Begruessung und Budget-Eingabe ---
name = input("Hallo! Gib mir deinen Namen: ")
print(f"Willkommen, {name}!\n")

running = True

while running:

    # --- Budget-Eingabe ---
    while True:
        try:
            budget = float(input("\nWie gross ist dein Budget (EUR)? ").replace(",", "."))
            if budget > 0:
                break
            print("Budget muss positiv sein!")
        except ValueError:
            print("Bitte nur Zahlen eingeben!")

    print("\n------------------------------------\n")

    # --- 3 Artikel einlesen (Dictionary) ---
    # Fuer jeden Artikel: Name, Stueckpreis, Menge
    # Zwischensumme = Summe aller Positionspreise
    artikel_dict = {}
    zwischensumme = 0.0

    for i in range(1, 4):
        artikel_dict[i] = {}
        print(f"{i}. Artikel:\n")

        # Artikelname
        artikel_dict[i]["name"] = input("Artikelname: ")

        # Stueckpreis mit Validierung
        while True:
            try:
                preis = round(float(input("Stueckpreis (EUR)? ").replace(",", ".")), 2)
                if preis >= 0:
                    artikel_dict[i]["preis"] = preis
                    break
                print("Preis muss positiv sein!")
            except ValueError:
                print("Bitte nur Zahlen eingeben!")

        # Menge mit Validierung
        while True:
            try:
                menge = int(input("Menge (Stueck)? "))
                if menge >= 0:
                    artikel_dict[i]["menge"] = menge
                    break
                print("Menge muss positiv sein!")
            except ValueError:
                print("Bitte nur ganze Zahlen eingeben!")

        # Positionspreis berechnen und anzeigen
        positionspreis = artikel_dict[i]["preis"] * artikel_dict[i]["menge"]
        zwischensumme += positionspreis
        print(f"\nHinzugefuegt: {artikel_dict[i]['name']}: {artikel_dict[i]['preis']:.2f} EUR x {menge} = {positionspreis:.2f} EUR")
        print(f"Zwischensumme: {zwischensumme:.2f} EUR\n")

    print("\n------------------------------------\n")

    # --- Rabattauswahl (mehrfache Verzweigung) ---
    print("0: Kein Rabatt")
    print("1: Student    – 10% Rabatt")
    print("2: VIP-Kunde  – 15% Rabatt")
    print("3: Gutschein  –  5 EUR (ab 20 EUR Einkaufswert)")

    while True:
        try:
            rabatt = int(input("\nRabatt-Auswahl (0-3): "))
            if 0 <= rabatt <= 3:
                break
            print("Bitte eine Zahl zwischen 0 und 3 eingeben!")
        except ValueError:
            print("Bitte nur ganze Zahlen eingeben!")

    print("\n------------------------------------\n")

    # --- Rabatt berechnen ---
    if rabatt == 0:
        summe = zwischensumme
        rabtext = "Kein Rabatt"
        rabsum = 0.0
    elif rabatt == 1:
        rabsum = -round(zwischensumme * 0.10, 2)
        summe = zwischensumme + rabsum
        rabtext = "Student -10%"
    elif rabatt == 2:
        rabsum = -round(zwischensumme * 0.15, 2)
        summe = zwischensumme + rabsum
        rabtext = "VIP -15%"
    else:
        # Gutschein nur ab 20 EUR einloesbar
        if zwischensumme < 20:
            print("Gutschein erst ab 20 EUR einloesbar – wird nicht angewendet.")
            summe = zwischensumme
            rabtext = "Kein Rabatt"
            rabsum = 0.0
        else:
            rabsum = -5.0
            summe = zwischensumme - 5
            rabtext = "Gutschein -5 EUR"

    summe = round(summe, 2)

    # ==========================================================================
    # QUITTUNG AUSGEBEN
    # ==========================================================================
    print("\n" * 3, "*" * 60)
    print(f"{'Q U I T T U N G':^60}")
    print("*" * 60)
    print(f"\nKunde: {name}\n")
    print("Artikel:")
    for i in range(1, 4):
        n = artikel_dict[i]["name"]
        p = artikel_dict[i]["preis"]
        m = artikel_dict[i]["menge"]
        print(f"  {i}. {n:.<35}{p:>5.2f} EUR x {m:>3} = {p*m:>7.2f} EUR")

    print("\n" + "=" * 60)
    print(f"\n  Zwischensumme:{zwischensumme:>42.2f} EUR")
    print(f"  Rabatt ({rabtext}):{rabsum:>40.2f} EUR")
    print(f"\n  Endsumme:{summe:>48.2f} EUR")
    print(f"  Budget:{budget:>50.2f} EUR")

    # Budgetkontrolle (einfache Verzweigung)
    budget -= summe
    if budget >= 0:
        print(f"  Restbudget:{budget:>46.2f} EUR")
        print(f"\n  Status: OK")
    else:
        print(f"\n  Status: NICHT GENUG GELD!")

    print("\n" + "*" * 60 + "\n")

    # --- Nochmal einkaufen? ---
    while True:
        again = input("\nNochmal einkaufen? (j/n): ").lower()
        if again == "n":
            print("\nWir freuen uns auf deinen naechsten Besuch!")
            running = False
            break
        elif again == "j":
            break
        else:
            print("\nBitte nur j oder n eingeben!")
