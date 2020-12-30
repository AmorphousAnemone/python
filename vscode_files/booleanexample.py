# print(42 == 42)
# print(42 == 99)
# print(2 != 3)
# print(2 != 2)

while True:
    # if not float or int
    num = input('Please enter a number from 1 to 10: ')
    if int(num) <= 10 and int(num) > 0:
        print('Well done')
        break
    print('Please try again...')
    
print('end')