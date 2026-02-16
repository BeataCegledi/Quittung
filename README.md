# Quittung
Mini-Shop-Kasse mit Rabatt &amp; Quittung Du programmierst eine Kassen-Anwendung in der Konsole. Der Nutzer gibt mehrere Artikel ein, wählt am Ende eine Rabattregel und bekommt eine saubere Quittung. Dabei nutzt du: Taschenrechner-Operationen, Eingaben, Verkettung/Formatierung von Ausgaben, einfache &amp; mehrfache Verzweigungen.
ungen.
## Funktionsumfang (Pflicht)
### Teil A – Start & Eingaben
Begrüßung, Name abfragen:
Ausgabe z. B.: Willkommen, Lea!
Frage nach dem Budget (Zahl, z. B. 50.00)
### Teil B – Artikel erfassen (3 Artikel)
Der Nutzer gibt genau 3 Artikel ein. Für jeden Artikel:
Artikelname (Text)
Stückpreis (Kommazahl)
Menge (Ganzzahl)
## Rechenregeln:
Positionspreis = Stückpreis * Menge
Zwischensumme = Summe aller Positionspreise
Ausgabe nach jedem Artikel (verkettet/formatiert):
z. B. Hinzugefügt: Apfel | 0.50 € x 6 = 3.00 €
### Teil C – Mehrfache Verzweigung: Rabatt auswählen
Der Nutzer wählt eine Rabattart:
Kein Rabatt
Student → 10% Rabatt
VIP → 15% Rabatt
Gutschein → fester Betrag (z. B. 5 €) (nur wenn Zwischensumme ≥ 20 €)
Wichtig: Nutze if/elif/else.
### Teil D – Einfache Verzweigung: Plausibilitätschecks
## Zusätzliche Prüfungen:
Wenn ein Preis oder eine Menge negativ ist → Ausgabe:
Ungültige Eingabe! Preis und Menge müssen positiv sein.
(Du darfst hier das Programm beenden oder den Wert nochmal abfragen.)
Wenn Gutschein gewählt und Zwischensumme < 20 € →
Gutschein wird nicht angewendet und du gibst das auch aus.
### Teil E – Quittung (schöne Ausgabe)
Am Ende soll eine Quittung erscheinen:
Beispiel-Layout (du darfst es ähnlich machen):
===== QUITTUNG =====
Kunde: Lea
Artikel:
1) Apfel 0.50 € x 6 = 3.00 €
2) Brot 2.20 € x 1 = 2.20 €
3) Saft 1.80 € x 2 = 3.60 €
Zwischensumme: 8.80 €
Rabatt (Student 10%): -0.88 €
Endsumme: 7.92 €
Budget: 50.00 €
Restbudget: 42.08 €
Status: OK
====================
### Teil F – Entscheidung: Budget reicht?
Nutze if/else:
Wenn Endsumme > Budget → Status: NICHT GENUG GELD
Sonst → Status: OK
## Bonus
➔  Mehrfache Verzweigung: Zahlungsart
1 Bar → kein Aufschlag
2 Karte → 1% Aufschlag
3 Online → 2% Aufschlag
(Aufschlag nach Rabatt anwenden)
➔ Runden
Endsumme auf 2 Nachkommastellen runden
➔ Artikel-Check
Wenn Gesamtmenge aller Artikel > 10 → Extra-Rabatt 3% (zusätzlich)
➔ Fehlereingaben abfangen
Wenn jemand bei Rabatt eine falsche Zahl eingibt → nochmal fragen (statt sofort beenden)
Abgabe
Dein Programm erfüllt die Aufgabe, wenn:
es alle 3 Artikel sauber einliest und berechnet
if sowie if/elif/else sinnvoll eingesetzt werden
Ausgaben lesbar und „verkettet“/formatiert sind
Budget-Check korrekt funktioniert
Quittung vollständig ist
