import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import RPi.GPIO as GPIO
import threading
import time

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

i=0
sampling = 10  #current sampling rate
arrSampling = [10, 5, 1] #sampling rates

#button interrupt configuration
def btn_pressed(channel):
    global i, sampling
    if (GPIO.input(channel)==0):
        #print("Check") 
        i=i+1   
        sampling = arrSampling[i]
        if i == 2:
            i=-1

GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(26, GPIO.FALLING, callback = btn_pressed, bouncetime = 200)


def print_time_thread():
    #sampling rate addition
    thread = threading.Timer(sampling, print_time_thread)
    thread.daemon = True
    thread.start()

    # create an analog input channel on pin 1 for the temp sensor and pin 2 for LDR
    chan2 = AnalogIn(mcp, MCP.P2)
    chan1 = AnalogIn(mcp, MCP.P1)

    #temperature calculation in degrees
    degree = round((chan1.voltage - 0.5) * 100,2)
    stop = time.time()
    
    print('{:15s}{:15s}{:15s}{:15s}'.format(str(round(stop - begin)) + ' s', str(chan1.value), str(degree) + ' C', str(chan2.value)))

if __name__ == '__main__':
    print('Runtime        Temp Reading   Temp         Light Reading')
    begin = time.time()
    print_time_thread()
    while True:
        pass
