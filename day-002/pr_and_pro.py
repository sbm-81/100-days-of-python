# name=input("What's your name? ")
# print("Hello, " + name )

# age =112
# print("Your are " + age+ " years old.")


print("Welcome to the tip calculator!")
bill=input("What was the total bill? $")
tip=input("How much tip would you like to give? 10, 12, or 15?")
people=input("How many people to split the bill? ")
print("Each person should pay: $", round((float(bill)+float(bill)*(float(tip)/100))/float(people), 2))


