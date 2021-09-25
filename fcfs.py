class FCFS :
    
    def Calcurate(n):
        
        d = dict()
 
        for i in range(n):
            key = "P"+str(i+1)
            print("Process "+key)
            a = int(input("Enter Arrival Time for Process"+str(i+1)+": "))
            b = int(input("Enter Burst Time for Process"+str(i+1)+": "))
            print("==================================")
            l = []
            l.append(a)
            l.append(b)
            d[key] = l
 
        d = sorted(d.items(), key=lambda item: item[1][0])
 
        ET = []
        for i in range(len(d)):
        # first process
            if(i==0):
                ET.append(d[i][1][1])
 
        # get prevET + newBT
            else:
                ET.append(ET[i-1] + d[i][1][1])
 
        TAT = []
        for i in range(len(d)):
            TAT.append(ET[i] - d[i][1][0])
 
        WT = []
        for i in range(len(d)):
            WT.append(TAT[i] - d[i][1][1])
 
        avg_WT = 0
        for i in WT:
            avg_WT +=i
        avg_WT = (avg_WT/n)

        avg_TT=0
        for i in TAT:
            avg_TT +=i
        avg_TT=(avg_TT/n)

        print("\tProcess\t|\tArrival\t|\tBurst Time\t|\tCompletion Time\t|\tTurnAround Time\t|\tWaiting Time\t|")
        for i in range(n):
            print("\t",d[i][0],"\t|\t",d[i][1][0],"\t|\t",d[i][1][1],"\t\t|\t",ET[i],"\t\t|\t",TAT[i],"\t\t|\t",WT[i],"\t\t|")
        print("Average Waiting Time: ",avg_WT)
        print("Average Turnaround Time: ",avg_TT)


# if __name__ == "__main__" :
#     fcfs = FCFS()