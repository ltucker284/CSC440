"""
This script simulates the round robin scheduling process for a predetermined set of 5 
processes and outputs their progress as execution time is incremented as well as
the start time, end time, initial wait time, and total wait time for each process.

Class: CSC 440
Authors: Juan Matiz, Liz Tucker
"""
from collections import deque

# pass in any number of iterable items
def create_deque(*iterables):
    process_deque = deque()
    for process in iterables:
        for process_info in process:
            process_deque.append(process_info)
    return process_deque

def round_robin(process_deque):
    start_time = 0
    quantum = 15
    answer_dict = dict()
    up_next = deque()
    queue = deque()
    # create a do while loop that continues until each process has been 'serviced'
    while process_deque[0][2] >= 0 and len(process_deque) != 0:
        
        #if a process has arrived, bring it in for service
        if process_deque[0][1] <= start_time:
            if process_deque[0][0] not in answer_dict:
                answer_dict[process_deque[0][0]] = {}    
                answer_dict[process_deque[0][0]]['Start Time'] = start_time
            #give it a place in line
            queue.append(process_deque[0])
            queue.rotate(-1)
            print(queue)
            process_deque.popleft()
            #decrement service time
            queue[0][2] = queue[0][2] - quantum
            #increment time
            start_time += quantum
            #if a process is done, pop it for good
            if queue[0][2] <= 0:
                answer_dict[queue[0][0]]['End Time'] = start_time
                queue.popleft()
            else:
                #put it at the end of the line
                queue.rotate(-1)
        #if a process isn't ready, ignore it and process what's already there
        else: 
            start_time+=quantum
            queue[0][2] = queue[0][2] - quantum
            queue.rotate(-1)

        print(f"Execution Time: {start_time}", queue)
        if len(process_deque) == 0:
            break
    
    return answer_dict

# calculate the initial wait time of a process
def calculate_init_wait(arrival_time, start_time):
    return start_time - arrival_time

# calculate the total wait time of a process
def calculate_total_wait(end_time, service_time, arrival_time):
    return end_time - service_time - arrival_time

def main():
    process_list = [[1,0,75],[2,10,40],[3,10,25],[4, 80,20],[5,85,45]]
    process_dict = {
        1:{
            "Service Time":75,
            "Arrival Time":0
        },
        2:{
            "Service Time":40,
            "Arrival Time":10
        },
        3:{
            "Service Time":25,
            "Arrival Time":10
        },
        4:{
            "Service Time":20,
            "Arrival Time":80
        },
        5:{
            "Service Time":45,
            "Arrival Time":85
        }
    }
    # create a deque of processes for round robin
    process_deque = create_deque(process_list)
    # store the answer dictionary which is the return value of the round_robin function
    answer_dict = round_robin(process_deque)

    # for every process in the answer dict, do the stuff below
    for entry in answer_dict:
        # get the initial wait time for each process
        answer_dict[entry]['Initial Wait Time'] = calculate_init_wait(process_dict[entry]['Arrival Time'], answer_dict[entry]['Start Time'])
        # get the total wait time of all the processes
        # answer_dict[entry]['Total Wait Time'] = calculate_total_wait(answer_dict[entry]['End Time'], process_dict[entry]['Service Time'], process_dict[entry]['Arrival Time'])
    # print the dict
    print(f"Answers: {answer_dict}")

if __name__ == "__main__":
    main()