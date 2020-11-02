binary_number=[1,1,1,1,0]
index=0
sum=0
a=0
while index < (len(binary_number)):
    sum=sum + (2**index *binary_number[-a])
    index=index+1
print(sum)