import mysql.connector

# Connect to database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Super7898$$#",
    database="serviceDB"
)

def selectrecords():
    cursorObject = dataBase.cursor()
    sql = "SELECT * FROM tbl_service"
    cursorObject.execute(sql)
    
    # print all the records
    for record in cursorObject.fetchall():
        print(record)


def updatetables():
    oldrowname = input("Enter old service name: ")
    newrowname = input("Enter new service name: ")
    
    cursorObject = dataBase.cursor()
    
    # Use placeholders (%s) for values
    sql = "UPDATE tbl_service SET Services = %s WHERE Services = %s"
    values = (newrowname, oldrowname)
    
    cursorObject.execute(sql, values)
    dataBase.commit()
    
    print("✅ Data updated in tbl_service successfully.")


# Run the functions
updatetables()
selectrecords()

# Close connection
dataBase.close()

