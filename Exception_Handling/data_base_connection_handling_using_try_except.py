#use of exception handling to test database connection and python connected or not
try:
    import mysql.connector
    query="create database feb15_db"
    db=mysql.connector.connect(host="localhost",user="venkat",password="mysql")
    cur=db.cursor()
    cur.execute(query)
    db.commit()
except:
    print("probably database connection failed due to wrong connection string parameters")
