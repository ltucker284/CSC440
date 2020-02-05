import os

print('I\'m about to create a child process, my pid is ' + str(os.getpid()))

###TODO use os.fork to create child process here

print('I am a child process, my pid is ' + str(os.getpid()) + '. My ppid is ' + str(os.getppid()))

###TODO make the child process sleep for 20 seconds and then exit

print('The child has terminated, my pid is ' + str(os.getpid()))

###TODO terminate the program