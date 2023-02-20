'''
lab 5
if statement 
'''

#3.1
alien_color= 'red'

if alien_color == 'green':
    print('you got 5 points')
#3.2
if alien_color == 'green':
    print('you got 5 points')
else:
    print('if you get 10 points')
#3.3
favorite_fruits=['grapes','blackberries','apple']
if 'apple' in favorite_fruits:
    print('you really like apple')
if 'blackberries' in favorite_fruits:
    print('you really like blackberries')
if 'grapes' in favorite_fruits:
    print('you really like grapes')
#3.4
age = 45

if age<10:
    print('person is a kid')
elif 10<age<20:
    print('person is a teenager')
else:
    print('person is an adult')
    if 65<age:
         print('person is an elder')
     