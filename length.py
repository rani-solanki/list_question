string=["rani","softwareEngineering","devlopers","coder"]
index=0
while(index<len(string)):
    increment=0
    count=0
    while(increment<len(string[index])):
        count=count+1
        increment=increment+1
    print(count,string[index])
    index=index+1