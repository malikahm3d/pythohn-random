people = ['malk', 'not malik', 'somene else']
numbers = [2, 45, 69]
people.extend(numbers)
print(people)

isMale = False
isTall = False
if isMale and isTall:
    print('tall male')
elif isMale and not(isTall):
    print("short male")
elif not(isMale) and isTall:
    print("tall female")
else:
    print("short female")