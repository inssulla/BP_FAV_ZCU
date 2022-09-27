print('Hello PyCharm')

print('This is the test file, if you understand that write the answer')

while True:
    answer = input('Write "Yes" or "No": ')
    if answer == "Yes":
        print('Great!')
        break
    elif answer == "No":
        print('Try one more time..\n')
        continue
    else:
        print('You have just 2 options...\n')
        continue