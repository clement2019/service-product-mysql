# importing required libraries
import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="Super7898$$#",
  database = "serviceDB"
)

# preparing a cursor object
cursorObject = dataBase.cursor()
 
# creating table 
Records = """CREATE TABLE tbl_service (
             Id INT NOT NULL AUTO_INCREMENT,
             Services VARCHAR(255) NOT NULL,
             PRIMARY KEY (Id)
                   )"""
 
# table created
cursorObject.execute(Records) 
print("Service table created successfully")
# disconnecting from server
dataBase.close()