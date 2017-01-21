#!/usr/bin/python
# -*- coding: utf-8 -*-
import multiprocessing
import psycopg2
import sys
import time
import os # for urandom
from base64 import b64encode # for urandom

# conn = None

# try:

# 	conn = psycopg2.connect("dbname='task2' user='dean'")
# 	cursor = conn.cursor()

# 	cursor.execute("DROP TABLE IF EXISTS Messages")
# 	cursor.execute("CREATE TABLE Messages(Id INT PRIMARY KEY, process_id INT, message TEXT)")

# 	conn.commit()


# except psycopg2.DatabaseError, e:

# 	if conn:

# 		conn.rollback()

# 	print 'Error %s' % e 
# 	sys.exit(1)


# finally:

# 	if conn:
# 		conn.close()



def worker1():


	# while True:

	# 	conn = psycopg2.connect("dbname='task2' user='dean'")        #  insert every 3 seconds !!!!!!!
	# 	cursor = conn.cursor()
	# 	time.sleep(3)
	# 	rand = os.urandom(5)
	# 	rand = b64encode(rand).decode('utf-8')
	# 	print rand
	# 	cursor.execute("INSERT INTO messages (message) VALUES (%s,)", (rand))
		

	# 	conn.commit()



	while True:

		
		conn = psycopg2.connect("dbname='task2' user='dean'")
		cursor = conn.cursor()
		#cursor.execute("INSERT INTO messages VALUES (1, 1, 'running')")  #used only to write into db

		cursor.execute("""SELECT * FROM Messages WHERE process_id = 2""")
		c = cursor.fetchone()

		if 'a' in c[2]:
			print c[2] 
		elif 'a' not in c[2]:
			print 'message doesn\'t contain a letter "a"'
		else:
			print 'message not found'
		time.sleep(.5)
		conn.commit()



def worker2():

	while True:

		
		conn = psycopg2.connect("dbname='task2' user='dean'")
		cursor = conn.cursor()
		#cursor.execute("INSERT INTO messages VALUES (2, 2, 'stopping')")  #used only to write into db

		cursor.execute("""SELECT * FROM Messages WHERE process_id = 1""")
		c = cursor.fetchone()
		
		if 'b' in c[2]:
			print c[2] 
		elif 'b' not in c[2]:
			print 'message doesn\'t contain a letter "b"'
		else:
			print 'message not found'
		time.sleep(.5)
		conn.commit()


if __name__ == '__main__':
	p1 = multiprocessing.Process(target=worker1)
	p2 = multiprocessing.Process(target=worker2)
	p1.start()
	p2.start()



# import multiprocessing
# import psycopg2
# import sys
# import time

# con = None

# try:
     
#     con = psycopg2.connect("dbname='task2' user='dean'")   
    
#     cur = con.cursor()
  
#     cur.execute("CREATE TABLE Messages(Id INTEGER PRIMARY KEY, process_id INT, message VARCHAR(20))")


    
#     con.commit()
    

# except psycopg2.DatabaseError, e:
    
#     if con:
#         con.rollback()
    
#     print 'Error %s' % e    
#     sys.exit(1)
    
    
# finally:
    
#     if con:
#         con.close()










# names = ['Process 1', 'Process 2']

# def process(lock, q):
#     name = multiprocessing.current_process().name   
    
#     while True:

#         for name in names:

#             if name == 'Process 1':

#                 lock.acquire()
#                 print name
#                 time.sleep(5)
#                 lock.release()
#                 q.put('Hello')
          
             
#             elif name == 'Process 2':
#                 lock.acquire()
#                 print name
#                 time.sleep(.1)
#                 lock.release()
#                 q.put('Hello')



# if __name__ == '__main__':
     
#     q = multiprocessing.Queue() 
#     lock = multiprocessing.Lock()

#     p1 = multiprocessing.Process(name='Process 1',target=process, args=(lock, q))
#     p2 = multiprocessing.Process(name='Process 2',target=process, args=(lock, q)) 


#     procs = [p1, p2]

#     p1.start()
#     p2.start()
  
#     for p in procs:
#         p.join()

#     while q.empty() is False:
#         print q.get()