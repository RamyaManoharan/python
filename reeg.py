import re
str1="hello world"
match=re.match('hello',str1)
print(match)

str1="hello world"
match=re.match('world',str1)
print(match)

match=re.sub('o','#',str1)
print(match)

match=re.match('hel',str1)
print(match)

match=re.search(r'\s',str1)
print(match)

match=re.search(r'\S',str1)
print(match)

match=re.search(r'\d',str1)
print(match)

match=re.search(r'\D',str1)
print(match)

match=re.search(r'\A',str1)
print(match)

match=re.search(r'\w',str1)
print(match)

match=re.search(r'\W',str1)
print(match)

match=re.search(r'\Z',str1)
print(match)

match=re.search(r'\bwo',str1)
print(match)

match=re.search(r'\Bd',str1)
print(match)

match=re.search(r'.',str1)
print(match)

match=re.search(r'\*',str1)
print(match)

ip='112.345.54.4'
match=re.search(r'\d+\.\d+\.\d+\.\d+',ip)
print(match)
print(match.group(0))


match=re.search(r'[l]',str1)
print(match)
print(match.group(0))

ipv6='fe80::80c9:5d7a:b500:2312%24'
match=re.search(r'[a-fA-F0-9:%]+',ipv6)
print(match)

str1='email Id : call.del@airindia.in'
match=re.search(r'[a-zA-Z ]+:([a-zA-Z ]+\.[a-z]+@([a-z]+)\.[a-z]+)',str1)
print(match)
print(match.group(0))
print(match.group(1))
print(match.group(2))

str1='Landline Number : 011-24667473'
match=re.search(r'[a-zA-Z ]: ([0-9]+)-([0-9]+)',str1)
print(match)
print(match.group(0))
print(match.group(1))
print(match.group(2))


str1='(Monday to Saturday,0930 hrs. - 1730 hrs. IST)'
match=re.search(r'[a-zA-Z \(]+,([a-z0-9. -]+)[A-Z\)]+',str1)
print(match)
print(match.group(0))
print(match.group(1))

str1='Landline Number : 011-24667473'
str2='Landline Number : 011.24667473'
str3='Landline Number : 011*24667473'
match=re.search(r'[a-zA-Z ]: [0-9]+.[0-9]+',str1)
match1=re.search(r'[a-zA-Z ]: [0-9]+.[0-9]+',str2)
match2=re.search(r'[a-zA-Z ]: [0-9]+.[0-9]+',str3)
print(match)
print(match1)
print(match2)

                




