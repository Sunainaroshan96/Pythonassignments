dict = {'a' : "hey",'b' : "Hello",'c' : "i need food"}
l = ''
for x in dict :
    l+=(x+"="+dict.get(x)+";")
l = l[:-1]
print(l)