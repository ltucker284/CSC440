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

    while process_deque[0][2] >= 0:
        print(f"Execution Time: {start_time}", process_deque)
        if process_deque[0][1] <= start_time:
            if process_deque[0][0] not in answer_dict:
                answer_dict[process_deque[0][0]] = {}
                answer_dict[process_deque[0][0]]['Start Time'] = start_time
            process_deque[0][2] = process_deque[0][2] - quantum
            start_time += quantum
            if process_deque[-1][-1] <= 0:
                answer_dict[process_deque[-1][0]]['End Time'] = start_time
                process_deque.pop()
            process_deque.rotate(-1)
        else: 
            process_deque.rotate(-1)
        
        if len(process_deque) == 0:
            break
        
    return answer_dict

def calculate_init_wait(arrival_time, start_time):
    return start_time - arrival_time

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

    process_deque = create_deque(process_list)
    answer_dict = round_robin(process_deque)

    for entry in answer_dict:
        answer_dict[entry]['Initial Wait Time'] = calculate_init_wait(process_dict[entry]['Arrival Time'], answer_dict[entry]['Start Time'])
        answer_dict[entry]['Total Wait Time'] = calculate_total_wait(answer_dict[entry]['End Time'], process_dict[entry]['Service Time'], process_dict[entry]['Arrival Time'])
    print(f"Answers: {answer_dict}")

if __name__ == "__main__":
    main()