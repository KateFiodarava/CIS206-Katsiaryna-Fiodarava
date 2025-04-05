import sqlite3

def connect_db(db_name):
    """Connect to the SQLite database."""
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print("Error connecting to database:", e)
        return None

def list_tables(conn):
    """List all tables in the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [row[0] for row in cursor.fetchall()]
    return tables

def show_table_data(conn, table_name):
    """Display all records in the selected table with column names and row numbers."""
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]

        print("\n" + "-" * 50)
        print(f"Table: {table_name}")
        print(" | ".join(column_names))
        print("-" * 50)

        for idx, row in enumerate(rows):
            print(f"{idx}: {row}")
        print("-" * 50)

        return rows, column_names
    except sqlite3.Error as e:
        print("Error reading table:", e)
        return [], []

def insert_record(conn, table_name, column_names):
    """Insert a new record into the selected table."""
    values = []
    for col in column_names:
        val = input(f"Enter value for {col}: ")
        values.append(val)

    placeholders = ",".join(["?" for _ in column_names])
    try:
        conn.execute(f"INSERT INTO {table_name} ({','.join(column_names)}) VALUES ({placeholders})", values)
        conn.commit()
        print("Record inserted successfully!")
    except sqlite3.Error as e:
        print("Insert failed:", e)

def update_record(conn, table_name, rows, column_names):
    """Update a selected field in the table."""
    try:
        row_index = int(input("Enter row number to update: "))
        column_index = int(input("Enter column number to update (0 for first column): "))
        new_value = input(f"Enter new value for {column_names[column_index]}: ")

        primary_key_col = column_names[0]
        primary_key_val = rows[row_index][0]

        conn.execute(f"UPDATE {table_name} SET {column_names[column_index]} = ? WHERE {primary_key_col} = ?", (new_value, primary_key_val))
        conn.commit()
        print("Record updated!")
    except (IndexError, ValueError) as e:
        print("Invalid input. Try again.")
    except sqlite3.Error as e:
        print("Update failed:", e)

def delete_record(conn, table_name, rows, column_names):
    """Delete a selected row from the table."""
    try:
        row_index = int(input("Enter row number to delete: "))
        primary_key_col = column_names[0]
        primary_key_val = rows[row_index][0]

        conn.execute(f"DELETE FROM {table_name} WHERE {primary_key_col} = ?", (primary_key_val,))
        conn.commit()
        print("Record deleted.")
    except (IndexError, ValueError):
        print("Invalid row number.")
    except sqlite3.Error as e:
        print("Delete failed:", e)

def main():
    db_name = "northwind.db"
    conn = connect_db(db_name)
    if not conn:
        return

    tables = list_tables(conn)
    if not tables:
        print("No tables found.")
        return

    print("\nAvailable Tables:")
    for i, table in enumerate(tables):
        print(f"{i}. {table}")

    try:
        table_index = int(input("Select a table by number: "))
        table_name = tables[table_index]
    except (IndexError, ValueError):
        print("Invalid table selection.")
        return

    rows, column_names = show_table_data(conn, table_name)

    action = input("Choose an action: (I)nsert, (U)pdate, (D)elete or (Q)uit: ").strip().upper()

    if action == "I":
        insert_record(conn, table_name, column_names)
    elif action == "U":
        update_record(conn, table_name, rows, column_names)
    elif action == "D":
        delete_record(conn, table_name, rows, column_names)
    elif action == "Q":
        print("Exiting program.")
    else:
        print("Unknown option.")

    conn.close()

if __name__ == "__main__":
    main()
