# 🧾 Quittung – Mini-Shop-Kasse

Konsolenprogramm für eine einfache Ladenkasse mit Rabatt und Budgetkontrolle – entwickelt im Rahmen der Berufsschulausbildung zur Fachinformatikerin.

## Funktionsumfang

Der Nutzer gibt seinen Namen, sein Budget und 3 Artikel ein. Nach der Rabattauswahl wird eine formatierte Quittung ausgegeben und geprüft, ob das Budget ausreicht.

### Eingaben
- Name und Budget
- 3 Artikel mit Name, Stückpreis und Menge

### Rabattregeln
| Option | Bedingung | Rabatt |
|---|---|---|
| Kein Rabatt | – | 0% |
| Student | – | -10% |
| VIP | – | -15% |
| Gutschein | Nur ab 20 € Einkaufswert | -5 € |

### Ausgabe
- Formatierte Quittung mit allen Positionen
- Zwischensumme, Rabatt, Endsumme
- Restbudget und Status (OK / NICHT GENUG GELD)

## Verwendete Python-Konzepte
- `while`-Schleife (Eingabevalidierung + Hauptschleife)
- `for`-Schleife (Artikel einlesen + Quittungsausgabe)
- `try` / `except` (Fehlerbehandlung)
- `if` / `elif` / `else` (Rabattauswahl + Budgetkontrolle)
- Dictionary (Artikelspeicherung)
- f-Strings (formatierte Ausgabe)

## Ausführen

```bash
python quittung.py
```

> Voraussetzungen: Python 3.x, keine externen Bibliotheken
