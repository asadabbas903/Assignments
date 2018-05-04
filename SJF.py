number = int(input('Enter the number of process you want to run'))
queue = []
queue2=[]
queue3=[]
queue1=[]
processPerClock = []
for i in range(number):
    process = []
    name = raw_input('Enter the name of process ')
    process.append(name)
    queue1.append(name)
    A_Time = int(input('Enter the arrival time of the process '))
    process.append(A_Time)
    queue2.append(A_Time)
    B_Time = int(input('Enter the burst time of the process'))
    process.append(B_Time)
    queue3.append(B_Time)
    queue.append(process)
queue.sort(key=lambda x: x[1])
print(queue)
count = 0
ttt = 0
wt = 0
turnaround = 0
waiting = 0
#for i in range(100):
#     waiting = turnaround - queue[count][2]
 #       ttt = turnaround + ttt
  #      wt = waiting + wt
   #     count = count + 1
    #    print turnaround, waiting
    #if (count >= number):
       # break
while number != 0:
    temp = []
    for i in range(len(queue2)):
        if queue2[i] <= count :
            temp.append(queue3[i])
            minimumExecutionTime = min(temp)
	for j in range(len(queue3)):
		if queue3[j] == minimumExecutionTime:
			tmp = j
			for p in range(queue3[j]):
				processPerClock.append(queue1[j])
			queue1.remove(queue1[j])
			queue2.remove(queue2[j])
	count = count + queue3[tmp]
	queue3.remove(queue3[tmp])
	number = number - 1
        for i in range(len(queue1)):
            waiting.append(processPerClock.index("p" + str(i)))

averageWaitingsTime = float(sum(waiting) / len(queue1)

print "average waiting time: ", averageWaitingsTime

responseTimes = []
        for i in range(len(queue2)):
            responseTimes.append(waiting[i] - queue2[i])

        averageResponseTime = float(sum(responseTimes)) / len(queue2)

        print "average response time: ", averageResponseTime

        turnAroundTimes = []

        for i in range(len(queue2)):
            turnAroundTimes.append(
                (len(processPerClock) - processPerClock[::-1].index("p" + str(i)) - 1) - copyOfArrivalTimes[i])

        averageTurnAroundTime = float(sum(turnAround)) / len(queue2)

        print "average turnAround time: ", averageTurnAroundTime
print ('Average turnaround time is '),ttt/number
print ('Average waiting time is '),wt
