# Application to connect a PIR(Digital) sensor and print the status of Human presence.
import sys

sys.path.append('/home/pi/Adafruit-Raspberry-Pi-Python-Code-legacy/Adafruit_MCP230xx')

from Adafruit_MCP230XX import Adafruit_MCP230XX
import time
mcp = Adafruit_MCP230XX(busnum = 1, address = 0x21, num_gpios = 16)
# Set pins 0, 1 and 2 to output (you can set pins 0..15 this way)
mcp.config(0, mcp.INPUT)
mcp.pullup(0, 1)
while (True):
    i = mcp.input(0)
    time.sleep(1)
    if i == 1:
        print "person detect"
    if i == 0:
        print "person not detect"
