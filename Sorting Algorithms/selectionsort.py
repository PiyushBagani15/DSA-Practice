#selection sort
def sort(list):
    for i in range(len(list)-1):
        minpos=i
        for j in range(i,len(list)):
            if list[j]<list[minpos]:
                minpos=j
        list[i],list[minpos]=list[minpos],list[i]#swapping
        
        print(list)
list=[3,5,4,7,8,1]
sort(list)
print(list)

