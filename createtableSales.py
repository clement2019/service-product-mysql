# importing required libraries
import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="Super7898$$#",
  database = "serviceDB"
)
def showtables():
  
  cursorObject = dataBase.cursor()
  cursorObject.execute("SHOW TABLES")
  for i in cursorObject:
    if len(i)>0:
      
      print(i)
    else:
      print("no tables to display")  
# preparing a cursor object
cursorObject = dataBase.cursor()
 
# creating table a
Records = """CREATE TABLE Sales (
             SaleId INT NOT NULL AUTO_INCREMENT,
             Productname VARCHAR(255) NOT NULL,
             Price DECIMAL(10, 2) NOT NULL,
             PRIMARY KEY (SaleId)
                   )"""
 
# table created
cursorObject.execute(Records) 
print("Customers table created successfully")
showtables()
# disconnecting from server
dataBase.close()
