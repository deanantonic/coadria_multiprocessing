
import multiprocessing

import time


names = ['Process 1', 'Process 2', 'Process 3']

def process(lock, q):
    name = multiprocessing.current_process().name   
    
    while True:

        for name in names:

            if name == 'Process 1':

                lock.acquire()
                print name
                sys.stdout.flush()
                time.sleep(5)
                lock.release()
                q.put('Hello')

          
             
            elif name == 'Process 2':
                lock.acquire()
                print name
                time.sleep(.1)
                lock.release()
                q.put('Hello')
            
            else:
                lock.acquire()
                print name
                time.sleep(2)
                lock.release()
                q.put('Hello')
                                  

                
            



if __name__ == '__main__':
     
   
    q = multiprocessing.Queue() 
    lock = multiprocessing.Lock()

    p1 = multiprocessing.Process(name='Process 1',target=process, args=(lock, q))
    p2 = multiprocessing.Process(name='Process 2',target=process, args=(lock, q)) 
    p3 = multiprocessing.Process(name='Process 3',target=process, args=(lock, q))

    procs = [p1, p2, p3]

    p1.start()
 
 
    p2.start()
  

    p3.start()
  
    for p in procs:
        p.join()


    while q.empty() is False:
        print q.get()