import sqlite3

# Connecting to company.db
conn = sqlite3.connect("company.db", check_same_thread=False)

cursor = conn.cursor()

def get_result(sql_query):
    if sql_query == "CANNOT RETURN QUERY":
        return [], None
    else:
        try:
            cursor.execute(sql_query)
            rows = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]
            return rows, column_names
        except sqlite3.Error as e:
            print(e)
            print("SQLITE ERROR")
            return [], None
