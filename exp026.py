string=input("enter the string:")
print(string)
dict={}
for n in string:
    if n in dict:
        dict[n]+=1
    else:
        dict[n]=1
print(dict)
for k,v in dict.items():
    print(k,v)