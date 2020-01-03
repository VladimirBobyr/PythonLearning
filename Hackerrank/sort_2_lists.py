
list1 = [1,3,10,2,3]
list2 = [5,8,9]
list3 = list1 + list2

for i in range(len(list3)):
    for j in range(len(list3)):
        if list3[i] < list3[j]:
            a = list3[i]
            #b = list3[j]
            list3[i] = list3[j]
            list3[j] = a

print(list3)
    # for m,j in enumerate(list3):
    #    if list[i] < list3[j]:


