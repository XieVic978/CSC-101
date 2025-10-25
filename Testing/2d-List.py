list1 = [[1,2,3,4],[]]
newList=[]
for sublist in list1:
    if len(sublist)>0:
        pass
        total = 0
        for item in sublist:
            total+=item
        avg = total / len(sublist)
        newList.append(avg)

print(newList)