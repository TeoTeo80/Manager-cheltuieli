import sqlite3 

with sqlite3.connect(database) as conn:
    cursor = conn.cursor()
    