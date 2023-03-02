'''
lab7
'''

#3.1 
num = 0
while num <= 5:
    if num != 3:
        print(num)
    num += 1
    
#3.2
num = 5
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print(factorial)

#3.3
num = 1
sum = 0
while num <= 5:
    sum += num
    num += 1
print(sum)

#3.4
product = 1
for num in range(3, 9):
    product *= num
print(product)

#3.5
i =4
product = 1
while i<=8:
    product = product * i
    i = i +1
print(product)

#3.6
num_list = [12, 32, 43, 35]
while num_list:
    num_list.pop()
    print(num_list)
