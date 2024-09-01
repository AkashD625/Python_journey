# list are the collections of items of same or different data type enclosed in swuare braket and separeted by commas.
# li = [3,2,6,5,9]  # indexing starts from 0 .
# li1 = [3,5,"Akash",True]   # lenght is determieed by len(li1) function.
# print(li)
# print(li1)
# print(li[0])  # for single element where the value in '[]' is the index of that value.
# print(li1[2])
# print(li[-2])  #this means len(li)-2 = 5-2 =  3  , li[3] will be printed.
# print(len(li1))  # Lenght will be printed.


# List positining
#syntax -
   # li = [2,3,2,6,5,4,"Mahesh"]
   # print(start:end:jump)
   # start position , end position , jumping between the index



# List comprahension
# we can add the for loop and use if condition in the list.

# li2  = [i for i in range(5)]
# print(li2)

# li3 = [i*i for i in range(50) if i%2==0]
# print(li3)



#--------------------->List methods------------------
li = [2,6,5,9]
m = [3,2,15,23,645]
# li.append(5)
#li.sort(reverse=True)
# li.reverse()
# m=li
# m[0] = 30  # this will create the another copy of li named m having the same elements , if change the elements in m then it will change in li also
#m = li.copy()  # now elements will not change.

# li.extend(m) # joint m to li

# li.insert(1,300)
# print(li)

