import mysql.connector as SQLC

# Connect to MySQL
DataBase = SQLC.connect(
  host="localhost",
  user="root",
  password="Super7898$$#"
)

def showDBs():
  Cursor = DataBase.cursor()
  Cursor.execute("SHOW DATABASES")
  for i in Cursor.fetchall():
    if len(i)>0:
      
      print(i)
    else:
      print("No database to display")   
  
  
try:
   
  # Create a cursor object
  Cursor = DataBase.cursor()
  print("please enter the database to drop")
  dropDB=input()

  # Execute command to create the database
  Cursor.execute("DROP DATABASE " + dropDB)

  print("Database " + dropDB + " deleted successfully")
  # printing all the databases
  showDBs()
except Exception as e:
  #SQLC.connection.rollback()
  print(f"Error!! either {str(dropDB)} does not exists", "error")
finally:
 # finally closing the database connection
 DataBase.close()