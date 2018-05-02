number=int(input('Enter the number of process you want to run .. '))
queue=[]
for i in range (number):
    process=[]
    name=raw_input('Enter the name of process ')
    process.append(name)
    A_Time=int(input('Enter the arrival time of the process '))
    process.append(A_Time)
    B_Time=int(input('Enter the burst time of the process '))
    process.append(B_Time)
    queue.append(process)
queue.sort(key=lambda x:x[1])
print(queue)
count=0
ttt=0
wt=0
turnaround=0
waiting=0
print ('Turnaround Time \t Waiting Time')
for i in range (100):
    if(i>=queue[count][1]):
        i=i+queue[count][2]
        turnaround=i-queue[count][1]
        waiting=turnaround-queue[count][2]
        ttt=turnaround+ttt
        wt=waiting+wt
        count=count+1
        print turnaround,' \t \t \t ',waiting
    if(count>=number):
        break
print ('Average turnaround time is '),ttt/number
print ('Average waiting time is '),wt
