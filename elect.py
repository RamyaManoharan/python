unit_used = int(input("Enter units"))
if unit_used>0 and unit_used<=100:
    print((unit_used*0.015) + (unit_used*1))
elif unit_used>100 and unit_used<=200:
    print((unit_used*0.015) + (unit_used*1.5))
elif unit_used>200 and unit_used<=500:
    print((unit_used*0.015) + (unit_used*3))
else:
    print((unit_used*0.015) + (unit_used*5))


