x = [10, 20]
print(x[0])
# computer starts counting at 0 so if we want to print 10, we have to start at 0. 20 would be 1

x = [3, 8, 7, 0, 5, 5, 2, 1]
print(x[1])

my_list = [3, 7, 3]

for item in my_list:
    print(item)


my_list = [2, 3, 4, 5, 6, 7]
print(my_list)

my_list.append(100)
print(my_list)


my_list = []

for i in range(5):
    user_input = int(input("Enter an integer:"))
    my_list.append(user_input)

print(my_list)


plain_text = "This is a test. ABC abc"
for c in plain_text:
    x = ord(c)
    print(x, end="")


class character:
    """
    This is a video game character.
    """
    def __init__(self):
        """ Create my character """
        self.name = ""
        self.outfit = ""


def main():
    home_address = Address()
    home_address.name = "John Smith"


main()