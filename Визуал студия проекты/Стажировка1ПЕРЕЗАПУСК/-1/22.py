#a={}
#t=[]
#t=input()
#s=t.split()
#d=[]
#d.append(s.index )
#print(s)
#a=dict.items(s)
#print(a)
#Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.
from typing import Counter


t=[]
t=input()
s=[]
for word in t.split():
    c=""
    for letter in word:
        if letter.isalpha():#проверяет это слово или нет ибо эта команда проверяет символ буква или нет
            c+=letter.lower()#делает все заглавные буквы прописнми
    s.append(c)
d=Counter(s)
f={
    value: key
    for key , value
    in d.items()

}
#a=list(d)
print(d)
print(f)
a=list(f)
maxa=max(a)
print(maxa)

print('чаще всего')
print(f.get(maxa))
print('длинее всего')
print(max(d, key=len))