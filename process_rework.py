"""This script simulates the linux fork() function
that creates a child process via the os python module.
This module is part of the python standard library, and it is
used to interact with the host operating system via python functions.

CSC440
Authors: Juan Matiz, Liz Tucker
"""

import os
import signal
import sys
import time

def create_child_process(parent_process_id):
    """This function creates the child process"""
    pid = os.fork()  # os.fork() creates a child process. If succesful it returns 0, and the parent's process id.
    if pid:  # We do not care about the parent's process id, so we pass.
        pass
        # parent_process_id = os.getpid()
    else:
        child_process_id = os.getpid()  # Obtains the process id of the child process. 
        print(f"Hello, I am the child process. Here is my pid: {child_process_id}")
        time.sleep(20)  # Script waits 20 seconds before the child process is terminated. 
        terminate_child_process(child_process_id, parent_process_id)

def terminate_child_process(child_process_id, parent_process_id):
    """This function terminates the child process that was created."""
    if type(child_process_id) == "NoneType":  # os.fork() returns a None, and int. We want to keep the int. 
        pass
    else:
        os.kill(child_process_id, signal.SIG_DFL)  # os.kill() params = pid, signal indication. signal.SIG_DFL tells the process to quit. 
        print(f"The child process has been terminated. My pid is: {parent_process_id}")

def main():
    """This functioin handles the script logic"""
    parent_process_id = os.getpid()  # os.getpid() obtains the process id. 
    print(f"Hello, I am the parent process. Here is my pid: {parent_process_id}")
    user_input = input("Would you like to create a child process? (y/n) ")

    if user_input == "y":
        create_child_process(parent_process_id)
    else:
        print("Goodbye!")
        sys.exit()
    
if __name__ == "__main__":
    main() 