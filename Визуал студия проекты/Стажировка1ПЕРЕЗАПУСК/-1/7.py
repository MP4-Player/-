#Нужно вывести первые n строк треугольника Паскаля. В этом треугольнике на вершине и по бокам стоят единицы, а каждое число внутри равно сумме двух расположенных над ним чисел.
n=input()
n=int(n)
kolekzey=[]
for i in range(n):
    stroka=[1]*(i+1)
    for j in range(i+1):
        if j !=0 and j !=i:
            stroka[j]=kolekzey[i-1][j-1]+kolekzey[i-1][j]
    kolekzey.append(stroka)
print(kolekzey)

for T in kolekzey:
    print(T)