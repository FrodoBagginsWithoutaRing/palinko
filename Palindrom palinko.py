a= input("Zadaj palindrom: ")
str(a)
a=a.replace(" ", "")
a=str.lower(a)
a_1= a [:: -1]
if a == a_1:
    print("je to palindrom")
else:
    print("nie je to palindrom")

