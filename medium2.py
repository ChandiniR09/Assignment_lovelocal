#Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

l=[]
d={}
nums=[int(x) for x in input("Enter the array elements:").split()]  #take input array and store in list

#for checking frequency of each number in the list and store it in dictionary as each number as key and its frequency as value
for i in nums:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1

size=len(nums) #size of array

#Checking the frequency of the number in the dictionary which is more than  ⌊ size/3 ⌋ times.
for k,v in d.items():
    if v>(size//3):
        l.append(k)
print(l)
