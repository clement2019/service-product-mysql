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

# correct SQL syntax and parameter style
sql = "DELETE FROM tbl_service WHERE Services is not Null"
  # must be a tuple

cursorObject.execute(sql)

#  commit the change to actually save it
dataBase.commit()

print("Data deleted from tbl_service successfully")

# close the connection
dataBase.close()