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

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return "num 1 is largest " + str(num1)
        #or
        #return "num 1 is largest " , num1
        #the diffrenaces between comma and plus have led me down a dark patch of python history
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(4,3,3))

#dictionaries
num_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(num_grid[0][2])
for row in num_grid:
    #print(row)
    for col in row:
        print(col)

# try:
#     #value = 10 / 0
#     a = int(input("enter a NUMBER: "))
#     print(a)
# except Exception as e:
#     print('Error: ', e)

students_file = open('students.txt', 'a')
# for student in students_file.readlines():
#     print(student)
students_file.write('\nYezen - cs')
students_file.close()