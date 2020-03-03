#Author: Darshan Chheda (DC)
#Taken from: https://repl.it/@dc25/RoundRobin-PREEMPTIVE
#Import Dependencies
from collections import deque

def availableproc():
	for i in range(n):
		if process_queue[i][1] <= time:
			if process_queue[i][2] > 0 and status[i] != 'True':
				status[i] = 'True'
				return i
				break

process_queue = []
n = int(input("Enter the total number of processes:"))
total = 0
status = ['False']*n
tq = int(input("Enter the time quantum:"))
tat = [0]*n
bt = []
wt = []
for i in range(n):
	process_queue.append([])
	process_queue[i].append(i)
	print()
	process_queue[i].append(int(input("Enter the Arrival Time:")))
	process_queue[i].append(int(input("Enter the Burst Time:")))
	bt.append(process_queue[i][2])
	total+=process_queue[i][2]

process_queue.sort(key = lambda process_queue:process_queue[1])
time = 0
d = deque()
gantt = []
if len(d) == 0:
	pid = availableproc()
	if process_queue[pid][2] < 2:
		total-=process_queue[pid][2]
		time+=process_queue[pid][2]
	else:
		total-=tq
		time+=tq
	process_queue[pid][2]-=tq
	gantt.append(pid)
	if process_queue[pid][2] < 0:
		process_queue[pid][2] = 0
else:
	pid = 0
	status[pid] = 'True'
	if process_queue[pid][2] < 2:
		total-=process_queue[pid][2]
		time += process_queue[pid][2]
	else:
		total-=tq
		time+=tq
	process_queue[pid][2]-=tq
	gantt.append(pid)
	if process_queue[pid][2] < 0:
		process_queue[pid][2] = 0
status[pid] = 'True'
for i in range(n):
	p = availableproc()
	if p != None:
		d.append(p)
if process_queue[pid][2] > 0:
	d.append(pid)
	print("\n")
else:
	tat[pid] = time
while total > 0:
	if process_queue[d[0]][2] < 2:
		total = total - process_queue[d[0]][2]
		time+=process_queue[d[0]][2]
	else:
		total = total - tq
		time+=tq
	gantt.append(d[0])
	process_queue[d[0]][2]-=tq
	if process_queue[d[0]][2] < 0:
		process_queue[d[0]][2] = 0
		tat[d[0]] = time
		d.popleft()
	else:
		pid = d.popleft()
		for i in range(n):
			p = availableproc()
			if p != None:
				d.append(p)
		if process_queue[pid][2] != 0:
			d.append(pid)
		else:
			tat[pid] = time

print("PNO\tAT\tBT\tTAT\tWT")
for i in range(n):
	wt.append(tat[i] - bt[i])
	print(process_queue[i][0],'\t',process_queue[i][1],'\t',bt[i],'\t',tat[i],'\t',wt[i])

print("Average TAT:",sum(tat)/n)
print("Average WT:",sum(wt)/n)