# function called count_up that takes in two numbers
# prints all numbers from start to finish inclusive
# test with 5, 10

start = 5
end = 10

def count_up(start, end):
    for current_number in range (start, end + 1):
        print(current_number)

count_up(5, 10)


import random

my_number = random.randrange(50)
print(my_number)