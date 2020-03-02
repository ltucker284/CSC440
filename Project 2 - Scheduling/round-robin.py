from collections import deque

# pass in any number of iterable items
def round_robin(*iterables):
    start_time = 0
    quantum = 15
    process_deque = deque()
    # create while loop to check that all service times are greater than 0
    for process_id in iterables[0]:
        while iterables[0][process_id]['Service Time'] > 0:
            if iterables[0][process_id]['Arrival Time'] <= start_time and iterables[0][process_id] not in process_deque:
                process_deque.append(iterables[0][process_id])
                print(process_deque)
            process_deque[0]['Service Time'] = process_deque[0]['Service Time'] - quantum
            process_deque.rotate(-1)
            start_time += quantum
            print(start_time)
            if process_deque[0]['Service Time'] < 0:
                process_deque.popleft()

def main():
    process_dict = {
        1:{
            "Process Id": 1,
            "Service Time":75,
            "Arrival Time":0
        },
        2:{
            "Process Id": 2,
            "Service Time":40,
            "Arrival Time":10
        },
        3:{
            "Process Id": 3,
            "Service Time":25,
            "Arrival Time":10
        },
        4:{
            "Process Id": 4,
            "Service Time":20,
            "Arrival Time":80
        },
        5:{
            "Process Id": 5,
            "Service Time":45,
            "Arrival Time":85
        }
    }

    round_robin(process_dict)

if __name__ == "__main__":
    main()