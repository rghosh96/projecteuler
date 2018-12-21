#Define set of numbers to perform calculations on
userRange = input("Hello, how many numbers would you like to enter? ")
numbers = list(range(int(userRange)))

#iterate through list & find numbers divisible by 3 or 5, and add to sum
num = 0
for x in numbers:
    if x % 3 == 0 or x % 5 == 0:
        num = num + x


#print final sum
print("The sum of all multiples of 3 and 5 up until", userRange, "is:", num)
