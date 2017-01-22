#!/usr/bin/python
# -*- coding: utf-8 -*-
import multiprocessing
import psycopg2
import sys
import time
import os # for urandom
from base64 import b64encode # for urandom


conn = None

try:

 	conn = psycopg2.connect("dbname='task2' user='dean'")
 	cursor = conn.cursor()

	cursor.execute("DROP TABLE IF EXISTS Messages")
	cursor.execute("CREATE TABLE Messages(Id SERIAL PRIMARY KEY, process_id INT, message TEXT)")  #serial auto increments id field

	conn.commit()


except psycopg2.DatabaseError, e:

	if conn:

		conn.rollback()

	print 'Error %s' % e 
	sys.exit(1)


finally:

	if conn:
		conn.close()




def worker1():

	while True:
		name = multiprocessing.current_process().name  
		name = int(name[-1])
		conn = psycopg2.connect("dbname='task2' user='dean'")
		cursor = conn.cursor()


		rand = os.urandom(5)
		rand = b64encode(rand).decode('utf-8')
		rand = str(rand)
		cursor.execute("INSERT INTO messages (process_id, message) VALUES (%s, %s)", (name, rand))
		print 'Process 1 inserting random chars'
		conn.commit()  
		time.sleep(3)


		cursor.execute("""SELECT * FROM Messages WHERE process_id = 2""")   
		c = cursor.fetchone()	

		if 'a' in c[2]:
			print c[2] 
		elif 'a' not in c[2]:
			print 'message doesn\'t contain a letter "a"'
		else:
			print 'message not found'
		conn.commit()
		time.sleep(.5)


def worker2():

	while True:
		name = multiprocessing.current_process().name  
		name = int(name[-1])		
		conn = psycopg2.connect("dbname='task2' user='dean'")
		cursor = conn.cursor()


		rand = os.urandom(5)
		rand = b64encode(rand).decode('utf-8')
		rand = str(rand)
		cursor.execute("INSERT INTO messages (process_id, message) VALUES (%s, %s)", (name, rand))
		print 'Process 2 inserting random chars'
		conn.commit()  
		time.sleep(3)


		cursor.execute("""SELECT * FROM Messages WHERE process_id = 1""")
		c = cursor.fetchone()
		
		if 'b' in c[2]:
			print c[2] 
		elif 'b' not in c[2]:
			print 'message doesn\'t contain a letter "b"'
		else:
			print 'message not found'
		conn.commit()
		time.sleep(.5)

if __name__ == '__main__':
	p1 = multiprocessing.Process(target=worker1)
	p2 = multiprocessing.Process(target=worker2)
	p1.start()
	p2.start()
	p1.join()
	p2.join()



