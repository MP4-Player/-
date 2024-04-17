#Найдите три ключа с самыми высокими значениями в словаре my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
my_dict=dict(sorted (my_dict.items(),key=lambda x:x[1], reverse=True))
s=my_dict.keys()
print(s)
d=list(s)
print(d[0:3])