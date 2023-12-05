#Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

count=0
n=int(input('Enter the number:')) 
while n!=0: #Complete iteration for all non-negative numbers less than or equal to n
    num=n
    while num!=0:
        if num%10==1:       #Obtain the last digit of the number and check whether its 1
            count +=1       #If it is 1 increment the count value
        num= num//10        #Remove the last digit from the number
    n=n-1                   #Decrease the number by 1
print('Total= ',count)      #Print the number of 1 obtained

