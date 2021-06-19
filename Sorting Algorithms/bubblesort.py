#bubble sort
def sort(list):
    for i in range(len(list)-1,0,-1):#here we start  from (last -1) value to 0 and iteration is negative
        for j in range(i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
                #temp=list[j]
                #list[j]=list[j+1]
                #list[j+1]=temp
list=[3,5,4,7,8,1]
sort(list)
print(list)