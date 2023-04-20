import busio
import digitalio
import board
import time
import csv
from datetime import datetime
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
 
# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
 
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.CE0)
 
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
 
# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)

i = 0;

fields = ['date', 'time', 'voltage']
filename = "cvs_test1.csv"

# collect data every minute for 5 minutes
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    while i < 5:
        filename = "cvs_test1.csv"
        now = datetime.now()
        date = now.strftime("%m/%d/%Y")
        times = now.strftime("%H:%M")
        rows = [date, times, str(chan.voltage)]
        csvwriter.writerow(rows)
        print('Raw ADC Value: ', chan.value)
        print('ADC Voltage: ' + str(chan.voltage) + 'V')
        time.sleep(60)
        i += 1
    end = ['06/01/2023', '00:00', '0']
    csvwriter.writerow(end)
    print('Data saved to cvs_test1.csv')
