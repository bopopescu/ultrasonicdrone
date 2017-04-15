from Adafruit_BBIO.SPI import SPI
import Adafruit_BBIO.UART as UART
import time
import serial
import numpy as np
import scipy as sp
import peakutils

spi = SPI(0,0)
spi.mode = 1
spi.bpw = 8
spi.msh = 8000000
UART.setup("UART5")
ser = serial.Serial(port="/dev/tty5", baudrate=19200)
ser.close()
ser.open()
def put_in_reset():
	print "\nput in reset"
	print spi.xfer2([int("16",16),int("2F",16),int("01",16)])
def read_this_fifo(this, that):
	#print "\nread this fifo"
	#print "sent: 08", this, that, " 00. Got:"
	resp = spi.xfer2([int("08",16), int(str(this), 16), int(str(that), 16), int("00", 16)])
	print resp
	return resp
def put_out_reset():
	print "\nput out reset"
	print spi.xfer2([int("16", 16), int("2F", 16), int("00",16)])
def init_burst():
	print "\ninitializing burst"
	print spi.xfer2([int("1A",16),int("C8",16),int("8D",16)])
def rearm_burst():
	print "\nrearm burst"
	print spi.xfer2([int("1A",16), int("C8",16),int("00",16)])
def read_ctl():
	print "\nread control"
	print spi.xfer2([int("19",16),int("C8",16),int("00",16)])
def read_fifo():
	print "\nread fifo"
	print spi.xfer2([int("08",16),int("00",16),int("FF",16),int("00",16)])
def end_spi():
	print "\nrunning spi.close()"
	spi.close()
def read_burstmode():
	print "\nread burstmode"
	print spi.xfer2([int("19", 16), int("B3", 16), int("00", 16)])
def read_fifo_ctl():
	print "\nread fifo control"
	print spi.xfer2([int("19", 16), int("C5", 16), int("00", 16)])
def set_fifo_ctl():
	print "\nset fifo control"
	print spi.xfer2([int("1A", 16), int("C5", 16), int("05",16)])
def read_fifo_ptrmsb():
	print "\nread fifo msb"
	print spi.xfer2([int("19",16), int("DF",16), int("00", 16)])
def read_fifo_ptrlsb():
	print "\nread fifo lsb"
	print spi.xfer2([int("19",16), int("E1",16), int("00", 16)])
def read_stat_reg():
	print "\nread status register"
        resp = spi.xfer2([int("19",16), int("C1",16), int("00", 16)])
	print resp
	return resp
def write_dac_ctl():
	print "\nwrite dac control"
	print spi.xfer2([int("1A",16), int("E5",16), int("02",16)])
def wait():
	for i in range (0, 1000000):
		i=i
def check_vreg():
	print "\nchecking vreg"
	print spi.xfer2([int("19",16),int("C2",16),int("00",0)])
def config_power():
	print "\nconfigure power mode"
	print spi.xfer2([int("1A",16),int("C3",16), int("03",16)])		

def init():
	print "\ninitializing"
	print spi.xfer2([int("1A",16),int("92",16), int("05",16)])
	print spi.xfer2([int("1A",16),int ("93",16), int("82",16)])
	print spi.xfer2([int("1A",16), int("94",16), int("F2",16)])
	print spi.xfer2([int("1A",16), int("95",16), int("AE", 16)])
	print spi.xfer2([int("1A",16), int("96",16), int("F4", 16)])
	print spi.xfer2([int("1A",16), int("97", 16), int("FB",16)])
	print spi.xfer2([int("1A", 16), int("A1",16), int("1F",16)])
	print spi.xfer2([int("1A",16), int("A2", 16), int("64", 16)])
	print spi.xfer2([int("1A", 16), int("A3",16), int("41",16)])
	print spi.xfer2([int("1A",16), int("A4", 16), int("38", 16)])
	print spi.xfer2([int("1A", 16), int("A5",16), int("19",16)])
	print spi.xfer2([int("1A", 16), int("AF",16), int("0C",16)])
	print spi.xfer2([int("1A", 16), int("B1",16), int("0C",16)])
	print spi.xfer2([int("1A", 16), int("A7",16), int("C8",16)])
	print spi.xfer2([int("1A", 16), int("AA",16), int("C8",16)])
	print spi.xfer2([int("1A", 16), int("AC",16), int("C8",16)])
	print spi.xfer2([int("1A", 16), int("AE",16), int("C8",16)])
	print spi.xfer2([int("1A",16), int("B5",16), int("01",16)])
	print spi.xfer2([int("1A",16), int("B7",16), int("02",16)])
	print spi.xfer2([int("1A",16), int("E2",16), int("0B",16)])
	print spi.xfer2([int("1A",16), int("B9",16), int("BC",16)])
	print spi.xfer2([int("1A",16), int("B2",16), int("05",16)])
	print spi.xfer2([int("1A",16), int("B6",16), int("0F",16)])
def read_FIFO_buf():
	this = 0
	that = 1
	fifo = []
	resp = []
	print "checking response"
	print read_this_fifo(0,0)
	while((this != 3)):
	        resp = read_this_fifo(this, that)
	        if (resp[0] == 2):
			fifo.append(int(resp[1]))
		else:
			that = that - 1
	        if (that == 255):
	                this =1+this
	                that = 0
	        else:
	                that = that + 1
	resp = read_this_fifo(2, 255)
	fifo.append(int(resp[1]))
	return fifo

put_in_reset()
wait()
put_out_reset()
wait()
if (ser.isOpen()):
	print"serial open"
print str(int("00550100", 16))
ser.write("00550100")
print "command sent"
resp = ser.read()
print resp










"""
init()
wait()
resp = []
fifo = []
resp = read_stat_reg()
wait()
print resp
while((resp[1] != 0) | (resp[2] != 0)):
	resp = read_stat_reg()
	wait()
config_power()
set_fifo_ctl()
#write_dac_ctl()

if ser.isOpen():
	print "serial is open"



for num in range (0,1):
	init_burst()
	wait()
	wait()
	wait()
	fifo = read_FIFO_buf()
	print fifo
	read_fifo()
	rearm_burst()
	fifoarray = np.array(fifo, dtype=float)
	indices = peakutils.indexes(fifoarray, thres=.85, min_dist=15)
	print indices
	for i in indices:
		print("%s meters" % str(float((40 * int(i) * 1000000) * (343/2))/1000000000000))
	for j in range (0,10):
		wait()
put_out_reset()
"""
end_spi()
