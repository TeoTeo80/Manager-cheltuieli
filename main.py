import sqlite3 
from datetime import date

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


def delete_expense(expense_id):
    try:
        with sqlite3.connect(database) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM expenses WHERE id = ?" , (expense_id))
            conn.commit()
            print(f"Cheltuiala cu ID {expense_id} a fost stearsa!")
    
    except Exception as e:
        print(f"Eroare la stergere" , e)

def view_expenses_by_category(category):
    try:
        with sqlite3.connect(database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM expenses WHERE category = ?" , (category.upper(),))
            rows = cursor.fetchall()
            print(f"\n--- CHELTUIELI PENTRU: {category.upper()}---")
            for row in rows:
                print(f"ID:{row[0]} | SUMA: {row[1]} | DATA: {row[3]}")
    
    except Exception as e:
        print("Eroare la filtrare:" , e)




if __name__ == "__main__":
    setup_database()

comanda = "1"
# while comanda != "4":
#     print("\n--- MENIU ---")
#     print("1. Adaugă | 2. Vezi tot | 3. Total | 4. Ieșire")
#     comanda = input("Alege opțiunea: ")

#     if comanda == 1:
#         nume_produs = input("Ce ai cumparat?")
#         pret = float(input(f"Cat a costat {nume_produs}?" ))
            
#         data_input = input("Data (Enter pentru AZI / AAAA-LL-ZZ): ")
#         if data_input == "":
#             data_finala = date.today().isoformat()
#         else:
#             data_finala = data_input
#             add_expense(float(pret), nume_produs.upper(), data_finala)
#             print(f"Am salvat {nume_produs} la data de {data_finala}")
#             continue

#         if comanda == "2":
#             view_all_expenses()
#             continue

#         if comanda == "3":
#             get_total_spent()
#             continue

#         if comanda == "4":
#             print("Sistem închis. La revedere!")

while comanda != "6":
    print("\---MENU---")
    print("1. Adauga | 2. vezi tot | 3. Total | 4. Serge | 5. Filtrare categorie | 6. Iesire")
    comanda = input("Alege opțiunea: ")

    if comanda == "1":
        nume_produs = input("Ce ai cumparat?")
        pret = float(input(f"Cat a costat {nume_produs}?" ))
        data_input = input("Data (Enter pentru AZI / AAAA-LL-ZZ): ")

        if data_input =="":
            data_finala = date.today().isoformat
        else:
            data_finala = data_input

        add_expense(pret, nume_produs.upper(), data_finala)
        continue

    elif comanda == "2":
        view_all_expenses()
    
    elif comanda == "3":
        
        get_total_spent()
    
    elif comanda == "4":
        id_sters = input("Introdu ID-ul cheltuielii de șters: ")
        delete_expense(id_sters)
    
    elif comanda == "5":
        cat = input("Introdu categoria pentru filtrare: ")
        view_expenses_by_category(cat)

    elif comanda == "6":
         print("Sistem închis. La revedere!")