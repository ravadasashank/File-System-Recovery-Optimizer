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

import random

class DiskCrashSimulator:
    def __init__(self):
        self.files = ["file1.txt", "file2.txt", "important.doc"]
        self.backup = {}

    def simulate_crash(self):
        print("Simulating disk crash... Some files are lost!")
        crashed_files = random.sample(self.files, len(self.files) // 2)
        for f in crashed_files:
            print(f"Lost file: {f}")
        return crashed_files

    def recover_files(self, crashed_files):
        print("Attempting recovery...")
        for file in crashed_files:
            if file in self.backup:
                print(f"Recovered {file} from backup!")
            else:
                print(f"Failed to recover {file}, no backup available.")

    def backup_files(self):
        print("Backing up files...")
        for f in self.files:
            self.backup[f] = "File data"
        print("Backup completed.")

# Example Usage
simulator = DiskCrashSimulator()
simulator.backup_files()
crashed = simulator.simulate_crash()
simulator.recover_files(crashed)
