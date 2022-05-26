import serial

while True:
    with serial.Serial('/dev/ttyUSB0', 9600, timeout=1) as ser:
        while True:
            line = ser.readline()
            print(line)