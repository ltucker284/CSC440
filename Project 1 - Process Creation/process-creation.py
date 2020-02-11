import os
import time
import sys

print("I'm about to create a child process, my pid is " + str(os.getpid()))

# use os.fork to create child process here
pid = os.fork()
if pid == 0:
    print("I am a child process, my pid is " + str(os.getpid()) + ".\nMy ppid is " + str(os.getppid()))

# make the child process sleep for 20 seconds and then exit
time.sleep(20)
os._exit
print("The child has terminated, my pid is " + str(os.getpid()))

# terminate the program
sys.exit
