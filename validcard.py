import re
num = int(input())
for i in range(num):
    card = input()
    rep = re.findall(r'((\d)\2{3,})', card)
    if rep:
        print("Invalid")
        break
    match = re.match(r'[456][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}',card)
    if(match):
        print("Valid")
    else:
        print("Invalid")
