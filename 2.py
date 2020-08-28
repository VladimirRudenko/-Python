a = 1
b = 2
c = 3

list_ex = (a, b, c)
list_ex_2 = range(10)
# for item in list_ex_2:
#     print(item)

    # while  item == 9:
    #     print(item)
    #     item += 1
    # print('Item is '+ str(item))


for item in list_ex_2:
    if item % 2 == 0:
        print(item)
    elif item ==3:
        print('This is elif '+str(item) + '_____')
    else:
        print("this is else " + str(item))


try:
    item % 2 == 0
    print(item)
except SyntaxError:
    print('this is SyntaxError')


# print(a)
# print(b)
# print(c)

dry = 'DRY'
print(dry)