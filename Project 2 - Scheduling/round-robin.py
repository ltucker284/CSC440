
quantum = 15
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

def round_robin():
    start_time = 0
    