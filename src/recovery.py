import sqlite3

class Journal:
    def __init__(self, db_name="journal.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, operation TEXT, filename TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)"
        )
        self.conn.commit()

    def log_operation(self, operation, filename):
        self.cursor.execute("INSERT INTO logs (operation, filename) VALUES (?, ?)", (operation, filename))
        self.conn.commit()

    def get_logs(self):
        self.cursor.execute("SELECT * FROM logs")
        return self.cursor.fetchall()

# Example Usage
journal = Journal()
journal.log_operation("CREATE", "test.txt")
print(journal.get_logs())
