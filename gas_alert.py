import sys
from auth import MiBand3
import time
import os
import serial


MAC_ADDR = sys.argv[1]
print 'Attempting to connect to ', MAC_ADDR
band = MiBand3(MAC_ADDR, debug=True)
#band.setSecurityLevel(level = "medium")

# Authenticate the MiBand
if len(sys.argv) > 2:
    if band.initialize():
        print("Initialized...")
    band.disconnect()
    sys.exit(0)
else:
    band.authenticate()

# init serial port
ser = serial.Serial('/dev/ttyUSB0', 9600) 

if __name__ == '__main__':
    data = ser.read()
    if data == 'G':
        band.send_gas_alert("GAS!!!")
        print 'GAS!!!'
        time.sleep(5)
    else:
        print 'Clear!'