'''
Created on Nov 22, 2018

@author: bpr
'''

from subprocess import Popen, PIPE
from udpServer import serverInitialize
import threading
from multiprocessing import Queue


def getValues():
    process = Popen(["/home/osmc/repo/Adafruit_Python_DHT/examples/AdafruitDHT.py", "2302", "4"], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    return output

def runProcess():
    queueLock.acquire()
    result = getValues()
    queueLock.release()
    return result


queueLock = threading.Lock()

serverInitialize()
