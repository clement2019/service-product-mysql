import mysql.connector as SQLC

# Connect to MySQL
DataBase = SQLC.connect(
  host="localhost",
  user="root",
  password="Super7898$$#"
)

# Create a cursor object
Cursor = DataBase.cursor()

# Execute command to create the database
Cursor.execute("DROP DATABASE serviceDB")

print("ServiceDB database deleted successfully")