#  Quittung  Mini-Shop-Kasse

> Konsolenprogramm fr eine einfache Ladenkasse mit Rabattsystem und Budgetkontrolle  entwickelt im Rahmen der Berufsschulausbildung zur Fachinformatikerin Anwendungsentwicklung.

##  Projektbeschreibung

Dieses Programm simuliert eine Ladenkasse. Der Nutzer gibt seinen Namen, ein Budget und 3 Artikel ein. Nach der Rabattauswahl wird eine formatierte Quittung ausgegeben. Das Programm prft, ob das Budget ausreicht, und zeigt das verbleibende Restbudget an.

##  Funktionsumfang

### Eingaben
- Name und Budget
- 3 Artikel mit: Artikelname  Stckpreis  Menge
- Rabattauswahl

### Rabattregeln
| Option | Bedingung | Rabatt |
|---|---|---|
| Kein Rabatt |  | 0% |
| Student |  | 10% auf Zwischensumme |
| VIP-Kunde |  | 15% auf Zwischensumme |
| Gutschein | Nur ab 20  Einkaufswert | 5  fix |

### Ausgabe
- Formatierte Quittung mit allen Artikelpositionen
- Zwischensumme  Rabatt  Endsumme
- Restbudget und Status:  OK /  Nicht genug Geld

##  Verwendete Python-Konzepte

| Konzept | Anwendung im Projekt |
|---|---|
| `while`-Schleife | Hauptschleife + Eingabevalidierung |
| `for`-Schleife | Artikel einlesen (3) + Quittungsausgabe |
| `try` / `except` | Fehlerbehandlung bei allen Nutzereingaben |
| `if` / `elif` / `else` | Rabattauswahl + Budgetkontrolle |
| Dictionary | Artikel strukturiert speichern (Name, Preis, Menge) |
| f-Strings | Formatierte, ausgerichtete Quittungsausgabe |
| `.replace(",", ".")` | Komma-Eingabe bei Dezimalzahlen abfangen |

##  Ausfhren

```bash
python quittung.py
```

> **Voraussetzungen:** Python 3.x  Keine externen Bibliotheken ntig

##  ber die Entwicklerin

Dieses Projekt zeigt meine Fhigkeit, Datenstrukturen (Dictionary), Schleifen und Verzweigungen zu kombinieren, um eine praxisnahe Kassenanwendung mit vollstndiger Eingabevalidierung und formatierter Ausgabe zu entwickeln.
