#Download opitions: be in python shell
    #MySQL Yum: sudo yum install mysql-connector-python -> https://dev.mysql.com/downloads/repo/yum/
    #Tar from Source: tar xzf mysql-connector-python-2.1.5.tar.gz 
        #cd mysql-connector-python-2.1.5
        #sudo python setup.py.install
            #2.1.5 may need to be 2.7 or 3.6, 
            #documentation doesn't specfiy of version is for connector or pytghon
    
    
#import functions
from __future__ import print_function

from decimal import Decimal
from datetime import datetime, date, timedelta
import time 
import mysql.connector

#do I need?:
    #def main
    #catch

# Connect with the MySQL Server
cnx = mysql.connector.connect(user='root', password = 'ultra', host = 'local host', database='employees')

# Get two cursors
curA = cnx.cursor(buffered=True)
curB = cnx.cursor(buffered=True)

#vars
date = str(datetime.now())
h = 10
sp = .12

# Insert command 
query = ("INSERT INTO data VALUES (%s, %s, %s)", (date, h, sp))
curA.execute(query)


# Commit the changes
cnx.commit()

cnx.close()
