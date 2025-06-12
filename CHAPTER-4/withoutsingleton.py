class DatabaseConnection:
    def __init__(self):
        # Initialize the connection (simulated)
        self.connection = "Connected to database"

    def get_connection(self):
        return self.connection

# Usage
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1.get_connection())  # Output: Connected to database
print(db1 is db2)            # Output: False (different instances)