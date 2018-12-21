

#Define set of numbers to perform calculations on
userRange = input("Hello, how many numbers would you like to enter? ")
numbers = [0] * int(userRange)
#print(numbers)

numbers[0] = 0
numbers[1] = 1

x = numbers[0]
y = numbers[1]
i = 0

range = int(userRange)

#perform fibonacci, & use only even values; add sums
sum = 0
while x < int(userRange):
    if x % 2 == 0:
        #print (x, end=", ")
        sum = sum + x
    z = x + y
    x = y
    y = z
    #i = i + 1

print("The total sum of the even-valued terms is:", sum)
