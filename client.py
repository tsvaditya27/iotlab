#Client
import bluetooth
import time
bd_addr ="B8:27:EB:48:BB:65"

port=1
sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))
while True:
    text=raw_input("Enter Message:")
    sock.send(text)
    time.sleep(8.5)
    data=sock.recv()
    print "Received" % data
    time. sleep(0.5)
sock.close()