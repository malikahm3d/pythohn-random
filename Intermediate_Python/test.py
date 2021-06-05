my_list = [0,1,2,3,4,5,6,7,8]

print(my_list[1:5])
#from index 1 (inclusive) to index 5 (exclusive)
print(my_list[::2])
#print all, but every other one
print(my_list[0:5:2])
#print first to fifth, but every other one

for item in my_list:
    print(item)
#for loop on list
for item in my_list[::2]:
    print(item)
#for loop on list, but change step
i = 0
step = 2
while i <= len(my_list):
    print(my_list[i])
    i = i + step
#while loop with step