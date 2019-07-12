def palin(s1):
    rev=s1[::-1]
    if s1==rev:
        print("PAlindrome")
    else:
        print("Not a palindrome")


s=input()
palin(s)
