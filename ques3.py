 # question 3
# to convert minutes  

total_seconds=int(input('enter the no. of seconds: ')) #take input from user
minutes=total_seconds // 60 #integer divison for number of minutes
seconds=total_seconds % 60 # finding the remainder seconds using modulus function
print(minutes, 'minutes and', seconds, 'seconds',) 