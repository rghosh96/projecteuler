# This is my solution to project Euler problem 6

def diff(x):
    sum_of_squares = 0
    square_of_sum = 0
    x = int(x)
    for i in range(x+1):
        sum_of_squares += i*i
        square_of_sum += i
    else:
        square_of_sum = square_of_sum**2
    return square_of_sum - sum_of_squares

