list1=[1,2,3,4]
list2=[2,3,4,6]
i=0
list=[]
while(i<len(list1)):
    j=0
    while(i<len(list2)-1):
        if list1[i]!=list2[j]:
            list.append(list1[i])
        j=j+1
    i=i+1
print(list)
