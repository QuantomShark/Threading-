import threading
import time

class myThread(threading.Thread):
    def_init_(self,threadID,name,counter):
        tjreading.Thread._init_(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print"starting"+self.name
        #Get lock to synchronize threads
        threadlock.acquire()
        print_time(self.name, self.counter,3)
        #Free lock to release next thread
        threadLock.release()

    def print_time(threadName, delay, counter):
        while counter:
            time.sleep(delay)
            print("%s: %s" %(threadName,time.ctime(time.time())
            counter -= 1
            #counter = counter - 1

    threadLock = threading.Lock()
    threads = []


    # Create new threads
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)


    #start new threads
    thread1.start()
    thread2.start()

    #Add thread to thread list
    threads.append(thread1)
    threads.append(thread2)

    #Wait for all threads to complete
    for t in threads:
                  t,join()           
                  print"Exiting Main Thread"           
