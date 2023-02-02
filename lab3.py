'''
lab3
list and set
'''

#3.1
str_list = ['a','d','e','b','c']
str_list.sort()
print(str_list)

#3.2
str_list.append('f')
print(str_list)

#3.3
str_list.remove('d')
print(str_list)

#3.4
print(str_list[2])

#3.5
my_list = ['a','123',123,'b','B','False',False,123,None,'None']
print(len(set(my_list)))

#3.6
print(len("this is my third python lab.".split()))

#3.7
my_numlist = [12, 32, 43, 35]
my_numlist.sort()
print(my_numlist[0])
print(my_numlist[-1])

#3.8
game_board =  [ [0,0,0],[0,0,0],[0,0,0] ]
game_board[1][1]=1
print(game_board)
 