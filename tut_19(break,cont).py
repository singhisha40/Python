#break and continue 
#break statement skips the loop
#continue statement skips the iteration


# for i in range(1,12):
#    if(i == 11):
#     break
#    print("5 X",i, "=",5*i)

#sum of n numbers
a = int(input("Enter num\n"))
sum = 0
while(a > 0):
    sum = sum + a
    a = a - 1
print("Sum:\n",sum)

#factorial
a = int(input("Enter num\n"))
fact = 1
while(a > 0):
    fact = fact * a
    a = a - 1
print("Fact:\n",fact)


