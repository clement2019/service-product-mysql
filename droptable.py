import mysql.connector as SQLC

# Connect to MySQL
DataBase = SQLC.connect(
  host="localhost",
  user="root",
  password="Super7898$$#",
  database = "serviceDB"
)

# Create a cursor object
Cursor = DataBase.cursor()

# Execute command to create the database
Cursor.execute("DROP TABLE tbl_service")

print("table tbl_service dropped successfully")