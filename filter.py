odd=lambda x:x%2
print(odd(5))

lst1=[]
for i in range(100):

    lst1.append(i)

odd_obj = filter(odd,lst1)
print(list(odd_obj))
