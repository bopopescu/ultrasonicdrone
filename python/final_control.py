#!/usr/bin/python
from __future__ import print_function
from decimal import Decimal
from datetime import datetime, date, timedelta
import time
import mysql.connector
import random


cnx = mysql.connector.connect(user='root', password = 'ultra', host = 'localhost', database='drone_data')

# Get two cursors
curA = cnx.cursor(buffered=True)

#vars
date = str(datetime.now())
height = float((40 * int(10)) * (343/2))/1000000
speed = .12
fifo = 10


while(1):
	direction = random.randint(0,1)
	dif = random.randint(0,7)
	if(direction == 0):
		if(fifo >= dif):
			fifo = fifo - dif
	else:
		if(fifo+dif > 767):
			fifo = 767
		else:
			fifo = fifo + dif
	oldheight = height
	height = float((40 * int(fifo)) * (343/2))/1000000
	speed = float((height-oldheight)/.3)
	date = str(datetime.now())
	# Insert command 
	query = ("INSERT INTO data VALUES (%s, %s, %s)")
	curA.execute(query,(date, height, speed))


	# Commit the changes
	cnx.commit()
	time.sleep(.3)

cnx.close()
