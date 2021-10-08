import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import RPi.GPIO as GPIO
import threading
import time

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP.MCP3008(spi, cs)

wait = 10
waits = [10, 5, 1]

def btn_pressed(channel):
    global i, wait
    if (GPIO.input(channel)==0):
        print("Ha Gay")
    i += 1
    if i == 3:
        i = 0
    wait = waits[i]

GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(18, GPIO.FALLING, callback = btn_pressed, bouncetime = 200)

def print_time_thread():
    thread = threading.Timer(wait, print_time_thread)
    thread.daemon = True
    thread.start()
    chan1 = AnalogIn(mcp, MCP.P2)
    chan2 = AnalogIn(mcp, MCP.P1)
    end = time.time()
    temp = (chan2.voltage - 0.5) * 100
    print('{:15s}{:15s}{:15s}{:15s}'.format(str(round(end - start)) + ' s', str(chan2.value), str(round(temp, 2)) + ' C', str(chan1.value)))

if __name__ == '__main__':
    print('Runtime        Temp Reading   Temp         \
  Light Reading')
    start = time.time()
    print_time_thread()
    i = 0
    while True:
        pass