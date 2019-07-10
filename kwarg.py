def display_emp(**data):
    for k,v in data.items():
        print("{} \t :{}".format(k,v))

display_emp(id=1001,name="R",age=30)

