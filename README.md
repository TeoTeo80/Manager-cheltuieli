# Manager Cheltuieli

Aceasta este o aplicație simplă pentru gestionarea cheltuielilor, scrisă în Python. Aplicația utilizează SQLite pentru stocarea datelor local într-un fișier numit `expenses.db`.

## Cerințe
- Python 3.x instalat pe sistemul dumneavoastră.

## Cum se pornește aplicația

Pentru a rula aplicația din cod, urmați pașii de mai jos:

1. **Deschideți un terminal** (sau o fereastră de Command Prompt/PowerShell).
2. **Navigați către directorul proiectului**:
   ```bash
   cd calea/catre/T_Manager_cheltuieli_GIT
   ```
3. **Rulați scriptul principal**:
   ```bash
   python main.py
   ```
   *Notă: Pe unele sisteme (în special Linux sau macOS), comanda ar putea fi `python3 main.py`.*

## Funcționalități actuale
- Crearea automată a bazei de date și a tabelului `expenses` la prima rulare.
- Adăugarea de cheltuieli (sumă, categorie, dată).
- Vizualizarea listei complete de cheltuieli.
- Calcularea totalului cheltuit.

## Structura Proiectului
- `main.py`: Scriptul principal care conține logica aplicației și interacțiunea cu baza de date.
- `expenses.db`: Fișierul bazei de date SQLite (generat automat la rulare).
