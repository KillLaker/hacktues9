import serial
import time
from send_emails import send_emails

ser = serial.Serial("/dev/ttyACM0", 9600)



while True:
    data = ser.readline()
    data = int(data.decode)

    if data == 1:
        print("Card accepted")
        send_emails()
        time.sleep(2)
    if data == 0:
        #flash red
        print("Card denied")
        time.sleep(2)