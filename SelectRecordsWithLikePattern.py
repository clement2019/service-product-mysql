import mysql.connector

# Connect to database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Super7898$$#",
    database="serviceDB"
)

cursorObject = dataBase.cursor()

# Get user input
tablename = input("Enter table name: ")
pattern = input("Enter search pattern: ")

# ✅ Validate table name (avoid injection)
allowed_tables = ["tbl_service", "tbl_customers"]  # whitelist tables
if tablename not in allowed_tables:
    print("Invalid table name!")
    dataBase.close()
    exit()


sql = f"SELECT * FROM {tablename} WHERE Services LIKE %s"
values = (f"%{pattern}%",)

cursorObject.execute(sql, values)


results = cursorObject.fetchall()
if results:
    for row in results:
        print(row)
else:
    print("No matching records found.")

print(f"Records retrieved from {tablename} with search pattern '{pattern}' successfully.")


dataBase.close()