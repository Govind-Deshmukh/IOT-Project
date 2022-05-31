# SELECT * 
# FROM table 
# WHERE id = (SELECT MAX(id) FROM TABLE)
import mysql.connector

mydb = mysql.connector.connect(
	host = "remotemysql.com",
	user = "uJjQaBfJbk",
	password = "fVIWjMLvvE",
    database = "uJjQaBfJbk"
)


cursor = mydb.cursor(buffered=True)
cursor.execute("SELECT * FROM testiot WHERE id = (SELECT MAX(id) FROM testiot);")
records = cursor.fetchall()
data = records[0]

print(data)
mydb.commit()
