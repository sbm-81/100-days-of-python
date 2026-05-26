import random

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!','#','$','%','&','(',')','*','+']

# I have implemented the project in two ways
#Easy method, order is not randomized
lettersCount=int(input(r'''Welcome to the Password Generator!
How many letters would you like in your password?
'''))

numbersCount=int(input('How many numbers would you like in your password?\n'))

symbolsCount=int(input('How many symbols would you like in your password? \n'))

generatedLetter=random.choices(letters,k=lettersCount)
generatedNumber=random.choices(numbers,k=numbersCount)
generatedSymbol=random.choices(symbols,k=symbolsCount)


password=generatedLetter+generatedSymbol+generatedNumber

print(f"{password}")
print("Your ordered password is: " + ''.join(password))

# Hard method, order is randomized to avoid being hacked
passwordinList=random.shuffle(password)
print("Your randomized password with the built-in shuffle method is: " + ''.join(password))


#another way to do the hard method, manual way
#random order 
rand_order=[]

#random.sample() method is used to generate a list of unique random numbers from the specified range. nice
rand_order=random.sample(range(0,len(password)), len(password))
# print(rand_order)
passwordinList2=[password[i] for i in rand_order]

print("Your randomized password with the manual shuffle method is: " + ''.join(passwordinList2))
