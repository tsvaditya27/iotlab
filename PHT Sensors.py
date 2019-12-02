import sys
import BME280lib as BME
import time

sys.path.append('/home/pi/Adafruit-Raspberry-Pi-Python-Code-legacy/Adafruit_MCP230xx')

while True:
    (chip_id,chip_version) = BME.readBME280ID()
    print "Chip ID    :", chip_id
    print "Version    :", chip_version

    temperature, pressure, humidity = BME.readBME280All()
    print "Temperature:", temperature, "C"
    print "Pressure   :", pressure, "hPa"
    print "Humidity   :", humidity, "%"
    time sleep(2)