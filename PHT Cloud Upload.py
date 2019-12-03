import sys
import BME280lib as BME
import time
import urllib.request as ur

sys.path.append('/home/pi/Adafruit-Raspberry-Pi-Python-Code-legacy/Adafruit_MCP230xx')

while True:
    (chip_id,chip_version) = BME.readBME280ID()
    print "Chip ID    :", chip_id
    print "Version    :", chip_version

    temperature, pressure, humidity = BME.readBME280All()
    print "Temperature:", temperature, "C"
    print "Pressure   :", pressure, "hPa"
    print "Humidity   :", humidity, "%"
    url = 'https://api.thingspeak.com/update?api_key=<api_key>&field1='+str(temperature)+'&field2='+str(pressure)+'&field3='+str(humidity)
    ur.urlopen(url)
    time sleep(2)