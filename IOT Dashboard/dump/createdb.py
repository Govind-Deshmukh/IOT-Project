import mysql.connector

mydb = mysql.connector.connect(
	host = "remotemysql.com",
	user = "uJjQaBfJbk",
	password = "fVIWjMLvvE",
    database = "uJjQaBfJbk"
)


cursor = mydb.cursor()
cursor.execute("CREATE Table IF NOT EXISTS testiot (id INT AUTO_INCREMENT PRIMARY KEY, humidity FLOAT,temperature FLOAT, uvindex FLOAT, pressure FLOAT, irsensor INT);")
