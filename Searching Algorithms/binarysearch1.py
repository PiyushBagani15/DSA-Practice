#another way
pos=-1
def binary(list,n):
    lower=0
    upper=len(list)-1
    found=False
    while (lower<=upper and not found):
        mid=(lower+upper)//2
        if list[mid]==n:
            globals()['pos']=mid
            print("element found",pos)
            found=True
        else:
            if list[mid]<n:
                lower=mid+1
            else:
                upper=mid-1
    return  found
print(binary([1,2,8,9,11,78,567],78))