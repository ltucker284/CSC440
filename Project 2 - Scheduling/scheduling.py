import random
import sys
import time

def arrival_time(list_of_processes):
    arrival_time_dict = {}
    average_interarrival_time = 0
    for process in list_of_processes:
        interarrival_time = 4 + random.randint(4, 8)  # interarrival time is the time between successive arrivals.
        if process == list_of_processes[-1]:
            arrival_time_dict[process] = 0
        else:
            arrival_time_dict[process] = interarrival_time

    for process in arrival_time_dict:
        average_interarrival_time += arrival_time_dict[process]  # Adds the current interarrival time plus the next. 
        # if process == 0:
            
        process_info = (f"Interarrival time: {str(arrival_time_dict[process])}", f"Arrivalaverage_interarrival_time")
        arrival_time_dict[process] = process_info

    # print(arrival_time_dict)
    print(f"The average interarrival time is : {str(average_interarrival_time/len(list_of_processes))} ")

def service_time(list_of_processes):
    service_time_dict = {}
    average_service_time = 0
    for process in list_of_processes:
        service_time = 2 + random.randint(2,5)
        if process == list_of_processes[-1]:
            service_time_dict[process] = service_time
            pass
        else:
            service_time_dict[process] = service_time
    for time in service_time_dict:
        average_service_time += service_time_dict[time]
    print(f"The average service time is : {str(average_service_time/len(list_of_processes))}")

def main():
    list_of_processes = list(range(0,100))
    print(len(list_of_processes))
    arrival_time(list_of_processes)
    service_time(list_of_processes)
    


if __name__ == "__main__":
    main()