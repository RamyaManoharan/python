movie=["the holy grail","the life of brain","The meaning of life"]
years=[1975,1979,1983]
l=[]
for i in range(3):
    l.append(movie[i])
    for j in range(i+1):
        if i==j:
            l.append(years[i])
print(l)
    
