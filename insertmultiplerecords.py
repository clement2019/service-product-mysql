import mysql.connector

# Connect to the database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Super7898$$#",
    database="serviceDB"
)

cursorObject = dataBase.cursor()

# Correct SQL syntax
records = "INSERT INTO Customers (CustomerId, Customername, Email) VALUES (%s, %s, %s)"

# Use a list of tuples for multiple rows
values = [
    (1, 'John Doe', 'johndoe@yahoo.com'),
    (2, 'Bon Freight', 'bonfreight@yahoo.com'),
    (3, 'George Shepard', 'georgeshepard@yahoo.com'),
    (5, 'Lee Jung', 'leejung@yahoo.com')
]

# Execute many records at once
cursorObject.executemany(records, values)

# Commit changes
dataBase.commit()

print(f"{cursorObject.rowcount} records inserted into Customers table successfully.")

