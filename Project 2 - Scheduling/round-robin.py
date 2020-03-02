from collections import deque

process_id_list = [1, 2, 3, 4, 5]
service_time_list = [75, 40, 25, 20, 45]
arrival_time_list = [0, 10, 10, 80, 85]

# pass in any number of iterable items
def round_robin(*iterables):
    start_time = 0
    quantum = 15
    process_deque = deque()
    # create a deque of itearble objects
    while True:
        try:
            for process_id in iterables[0]:
                start_time += quantum
                if iterables[0][process_id]['Arrival Time'] <= start_time:
                    process_deque.append(iterables[0][process_id])
                print(process_deque)
        except StopIteration:
            process_deque.popleft()




    # while there's stuff in iterators, keep going
#     while iterators:
#         try:
#             # while True essentially means forever until there's nothing left to be done in the loop
#             while True:
#                 yield next(iterators[0])
#                 iterators.rotate(-1)
#         except StopIteration:
#             # Remove an exhausted iterator.
#             iterators.popleft()
    
# for value in round_robin(arrival_time_list, service_time_list):
#     print(value)

def main():
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

    round_robin(process_dict)

if __name__ == "__main__":
    main()