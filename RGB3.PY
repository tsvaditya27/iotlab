#mcp23017 library path
import sys
sys.path.append('/home/pi/Adafruit-Raspberry-Pi-Python-Code-legacy/Adafruit_MCP230xx')
from Adafruit_MCP230XX import Adafruit_MCP230XX
import time

#mcp IC configuration
mcp = Adafruit_MCP230XX(busnum = 1, address = 0x20, num_gpios = 16) # MCP23017

#mcp input/output configuration
mcp.config(0, mcp.OUTPUT)
mcp.config(1, mcp.OUTPUT)
mcp.config(2, mcp.OUTPUT)
mcp.config(3, mcp.OUTPUT)
mcp.config(4, mcp.OUTPUT)
mcp.config(5, mcp.OUTPUT)
mcp.config(6, mcp.OUTPUT)
mcp.config(7, mcp.OUTPUT)
mcp.config(8, mcp.OUTPUT)
mcp.config(9, mcp.INPUT)
mcp.config(11, mcp.OUTPUT)
mcp.pullup(9, 1)
while(True):
    mcp.output(0,0)
    mcp.output(4,0)
    mcp.output(8,0)
    x=mcp.input(9)
    y=mcp.input(10)
    #print(x,y)
    if x==0 and y==0:
        mcp.output(0,1)
        mcp.output(11,1)
    elif x==512 and y==0:
        mcp.output(4,1)
        mcp.output(11,1)
    elif y==1024 and x==0:
        mcp.output(8,1)
        mcp.output(11,1)
    else:
        mcp.output(11,0)
        """mcp.output(0,1)
        mcp.output(4,1)
        mcp.output(8,1)
        mcp.output(11, 1)
        time.sleep(2)
        mcp.output(0,0)
        mcp.output(4,0)
        mcp.output(8,0)
        mcp.output(11, 0)"""
