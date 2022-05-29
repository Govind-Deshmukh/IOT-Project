import serial
import mysql.connector

try:
    mydb = mysql.connector.connect(
        host = "remotemysql.com",
        user = "uJjQaBfJbk",
        password = "fVIWjMLvvE",
        database = "uJjQaBfJbk"
    )
except:
    print("Could not connect to database")
else:
  print("connected to database")



cursor = mydb.cursor()

# firest line humidity
# second line temp 
# third line UV index
# fourth line pressure 
# fifth line IR sensor (open 1 close 0)

while True:
    with serial.Serial('/dev/ttyUSB0', 9600, timeout=None) as ser:
        while True:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            lst = line.split(',')
            print(lst)
            try:
                cursor.execute("INSERT INTO testiot (humidity, temperature, uvindex, pressure, irsensor) VALUES (%s, %s, %s, %s, %s)", (lst[0], lst[1], lst[2], lst[3], lst[4]))
                mydb.commit()
            except:
                print("Could not insert data")
            else:
                print("Data inserted")

            #cursor.execute("INSERT INTO testiot (humidity, temperature, uvindex, pressure, irsensor) VALUES (%s, %s, %s, %s, %s)", (lst[0], lst[1], lst[2], lst[3], lst[4]))
            # INSERT INTO TABLE_NAME (humidity, temperature,uvindex,pressure,irsensor) VALUES (value1, value2, value3,...valueN);
