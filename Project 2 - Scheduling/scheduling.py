import random

def arrival_time(list_of_processes):
    arrival_time_dict = {}
    for process in list_of_processes:
        inter_arrival_time = 4 + random.randint(4, 8) 
        arrival_time_dict[process] = inter_arrival_time
    
    print(arrival_time_dict)

# def service_time(list_of_processes):
#     service_time_dict = {}
#     for process in list_of_processes:
#         service_time = 2 + random.randint(2,5)
#         pass

def main():
    list_of_processes = list(range(0,101))
    arrival_time(list_of_processes)
    # service_time(list_of_processes)
    


if __name__ == "__main__":
    main()