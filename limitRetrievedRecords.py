#SELECT * FROM Customers
#LIMIT 3;

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
print("enter table name")
tablename=input()
# correct SQL syntax and parameter style
sql = "SELECT * FROM " + tablename + " LIMIT 2"
  # must be a tuple

cursorObject.execute(sql)
# printing all the recoords
for i in cursorObject:
    print(i)

#  commit the change to actually save it
dataBase.commit()
#print(sql)
print("Records retrieved from " + tablename + " successfully")

# close the connection
dataBase.close()