# -*- coding: utf-8 -*-


with open(r'D:\ProgramFiles\PycharmProjects\learnpy\learnscrapy\esp.csv') as file:
    for line in file:
        my_list = line.split(',')
        with open(r'D:\ProgramFiles\PycharmProjects\learnpy\learnscrapy\new.csv', 'a') as new_file:
            for i, name in enumerate(my_list):
                if 2 <= i <= 17:
                    num = 1998 + i
                    print('{0},{1},{2},{3}'.format(my_list[0], my_list[1], str(num), name))
                    strings = my_list[0] + ', ' + my_list[1] + ', ' + str(num) + ', ' + name + '\n'
                    new_file.write(strings)

'''
file = open(r'D:\ProgramFiles\PycharmProjects\learnpy\learnscrapy\esp.csv')
while 1:
    line = file.readline()
    if not line:
        break
    my_list = line.split(',')
    new_file = open(r'D:\ProgramFiles\PycharmProjects\learnpy\learnscrapy\new.csv', 'a')
    for i, name in enumerate(my_list):
        if 2 <= i <= 17:
            num = 1998 + i
            print('{0},{1},{2},{3}'.format(my_list[0], my_list[1], str(num), name))
            strings = my_list[0] + ', ' + my_list[1] + ', ' + str(num) + ', ' + name + '\n'
            new_file.write(strings)
    new_file.close()

file.close()
'''




