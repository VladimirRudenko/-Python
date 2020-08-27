list_home = range(1, 101)
for item in list_home:
    if item % 3 == 0:
        print(str(item) + ' Fizz')
    elif item % 5:
        print(str(item) + " Buzz")
    else:

        print(str(item) + " FizzBuzz")