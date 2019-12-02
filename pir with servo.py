# Application to connect a PIR(Digital) sensor and print the status of Human presence.
import sys
import RPi.GPIO as GPIO
import time
from Adafruit_MCP230XX import Adafruit_MCP230XX

sys.path.append('/home/pi/Adafruit-Raspberry-Pi-Python-Code-legacy/Adafruit_MCP230xx')


mcp = Adafruit_MCP230XX(busnum = 1, address = 0x21, num_gpios = 16)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)

pwm=GPIO.PWM(22,100)
pwm.start(5)

angle1=160
duty1= float(angle1)/10 + 2.5

angle2=160
duty2= float(angle2)/10 + 2.5

mcp.config(0, mcp.INPUT)
mcp.config(11, mcp.OUTPUT)
mcp.config(6, mcp.OUTPUT)
mcp.pullup(0, 1)

while (True):
    i = mcp.input(0)
    time.sleep(0.2)
    if i == 1:
        print "person detect"
        mcp.output(11, 1)
	mcp.output(6, 1)
        pwm.ChangeDutyCycle(duty1)
        time.sleep(0.8)
        pwm.ChangeDutyCycle(duty2)
        time.sleep(0.8)
    if i == 0:
        print "person not detect"
        mcp.output(11, 0)
	mcp.output(6, 0)

GPIO.cleanup()