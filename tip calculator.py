print ("Welcome to the tip calculator.")
bill = int(input("What was the total bill? "))
per=int(input("what percentage tip would you like to give ? 10,12, or 15 "))
split = int(input("Enter number of people "))
per_1=  round((bill/split) + (bill* per/100), 2)
print ("Each person should pay: ", per_1)