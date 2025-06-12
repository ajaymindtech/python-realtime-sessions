class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            # Initialize the connection (simulated)
            cls._instance.connection = "Connected to database"
        return cls._instance

    def get_connection(self):
        return self.connection

# Usage
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1.get_connection())  # Output: Connected to database
print(db1 is db2)            # Output: True (both are the same instance)