import serial


# firest line humidity
# second line temp 
# third line UV index
# fourth line pressure 
# fifth line IR sensor (open 1 close 0)

while True:
    with serial.Serial('/dev/ttyUSB0', 9600, timeout=25) as ser:
        while True:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)

            INSERT INTO TABLE_NAME (humidity, temperature,uvindex,pressure,irsensor) VALUES (value1, value2, value3,...valueN);