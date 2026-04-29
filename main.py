import sqlite3 

# Configurări globale
database = 'expenses.db'

def setup_database():
    sql_statements = [
        """
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            amount REAL,
            category TEXT,
            date TEXT
        );
        """
    ]
    try:
        
        with sqlite3.connect(database) as conn:
            cursor = conn.cursor()
            for statement in sql_statements:
                cursor.execute(statement)
            conn.commit() 
            print("Baza de date este gata!")
    except Exception as e:
        print("Eroare la crearea tabelului:", e)

def add_expense(amount, category, date):
    try:
        with sqlite3.connect(database) as conn:
            cursor = conn.cursor()
            sql_insert = "INSERT INTO expenses(amount, category, date) VALUES (?, ?, ?)"
            cursor.execute(sql_insert, (amount, category, date))
            conn.commit()
            print(f"Am salvat cheltuiala: {category} - {amount} RON")
    except Exception as e:
        print("Eroare la inserare:", e)

def view_all_expenses():
    try:
        with sqlite3.connect(database) as conn:
            cursor = conn.cursor()
            sql_query = "SELECT * FROM expenses"
            cursor.execute(sql_query)
            rows = cursor.fetchall()
            print("\n--- LISTĂ CHELTUIELI ---")
            for row in rows:
                print(f"ID: {row[0]} | Sumă: {row[1]} | Categorie: {row[2]} | Dată: {row[3]}")
    except Exception as e:
        print("Eroare la citire:", e)

def get_total_spent():
    try:
        with sqlite3.connect(database) as conn:
            cursor = conn.cursor()
            sql_total = "SELECT SUM(amount) FROM expenses"
            cursor.execute(sql_total)
            result = cursor.fetchone()
            total = result[0] if result[0] is not None else 0
            print(f"\nTOTAL CHELTUIT: {total} RON")
    except Exception as e:
        print("Eroare la calcul total:", e)


if __name__ == "__main__":
    setup_database()

    #  Adăugăm cheltuieli 
    paine = (5.50, "Mancare", "2026-04-29")
    add_expense(*paine) # Folosim * pentru a desface tuplul
    
    apa = (3.00, "Bauturi", "2026-04-29")
    add_expense(*apa)

    # 3. Afișăm rezultatele
    view_all_expenses()
    get_total_spent()