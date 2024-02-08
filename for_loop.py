import time

# for loop : a statement that will execute its block of code
#            a limited amount of time
#
#            while loop  = unlimited
#            for loop = limited (we already know the amount of time)

#for i in range(10):
#    print(i+1)


# the 3rd argument is the step
#for i in range(20-1, 50, 2):
#    print(i+1)

#for i in "tauhid hasan":
#   print(i)

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)

# this line should be out of the for loop to be printed at the last after the countdown is finished.
print("Happy new year")


