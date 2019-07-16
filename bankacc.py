from functools import reduce
l = [[12354,'Computer Programming',5,449],[12355,'Programming for beginners',8,649],[12346,'Computer Basics',3,179]]
# l = []
# num = int(input("Enter number"))
# for i in range(num):
#     l.append(list(input("Enter items in a line").split()))

f = lambda x,y : int(x)*int(y)
for i in range(len(l)):
    print("({},{})".format(l[i][1],reduce(f,l[i][2:])))