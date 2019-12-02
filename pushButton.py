#mcp23017 library path
import sys
sys.path.append('/home/pi/Adafruit-Raspberry-Pi-Python-Code-legacy/Adafruit_MCP230xx')
from Adafruit_MCP230XX import Adafruit_MCP230XX
import time

#mcp IC configuration
mcp = Adafruit_MCP230XX(busnum = 1, address = 0x20, num_gpios = 16) # MCP23017

#mcp input/output configuration
mcp.config(0, mcp.OUTPUT)
mcp.config(4, mcp.OUTPUT)
mcp.config(8, mcp.OUTPUT)

mcp.config(9, mcp.OUTPUT)
mcp.pullup(9, 1)
mcp.config(10, mcp.OUTPUT)
mcp.pullup(10, 1)

try:
    while True:
	x = mcp.input(9)
	y = mcp.input(10)
	print "Pin 9  = %d" % x
	print "Pin 10 = %d" % y
	if x == 512:
            #RGB LED blink
    	    mcp.output(0, 1)
    	    mcp.output(4, 1)
    	    mcp.output(8, 1)
    	    time.sleep(1)
	    mcp.output(0, 0)
    	    mcp.output(4, 0)
    	    mcp.output(8, 0)
except KeyboardInterrupt:
    mcp.output(0, 0)
    mcp.output(4, 0)
    mcp.output(8, 0)