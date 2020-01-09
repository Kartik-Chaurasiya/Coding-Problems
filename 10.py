import threading
import time

def f():
	print("hii")

def jobshedular(f, n) :
	time.sleep(n/1000)
	f()

jobshedular(f, 1000)
