import mysql.connector

# connect to database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Super7898$$#",
    database="serviceDB"
)

# prepare a cursor object
cursorObject = dataBase.cursor()

#  correct SQL syntax and parameter style
sql = "INSERT INTO tbl_service (Services) VALUES (%s)"
val = ("cleaning",)  # must be a tuple

cursorObject.execute(sql, val)

#  commit the change to actually save it
dataBase.commit()

print("Data inserted into tbl_service successfully")

# close the connection
dataBase.close()