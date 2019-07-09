import random
name=input("Hello!Enter your name")
print(name)
print("Well {}, Iam thinking of a number 1 to 10\n".format(name))
k=random.randint(1,10)
for i in range(5):
    number = int(input("Take a guess"))
    
    if k>number:
        print("\n Too low")
    elif k<number:
        print("\n Too High")
    else:
        print("Win")
        
        break
    
