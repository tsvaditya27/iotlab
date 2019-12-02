import sys
import time

sys.path.append('/home/pi/Adafruit-Raspberry-Pi-Python-Code-legacy/Adafruit_MCP230xx')
from Adafruit_MCP230XX import Adafruit_MCP230XX

#mcp IC configuration
mcp = Adafruit_MCP230XX(busnum = 1, address = 0x20, num_gpios = 16) # MCP23017

#mcp input/output configuration
mcp.config(11, mcp.OUTPUT)

try:
    while True:
	mcp.output(11, 1)
	time.sleep(1)
	mcp.output(11,0)
	time.sleep(1)
except KeyboardInterrupt:
mcp.output(11,0)