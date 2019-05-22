import string

token_exprs=[";",":",","]
token_exprs_string=["begin","for","var","end","else","integer"]
token_const=["0","1","2","3","4","5","6","7","8","9","10"]
token_variables=[string.ascii_letters]
f=open("C:\\Users\\TopGamer\\Desktop\\Example.txt")
z=0
x=0
b=0
s=0
while 1:
    char=f.read(1)
    s=s+1
    if char in token_exprs:
        z=z+1
    if char in token_const:
        b=b+1   
    if not char:break
    
    
with open("C:\\Users\\TopGamer\\Desktop\\Example.txt") as f:
        for line in f:
            s1=set(line.split())
            s2=set(token_exprs_string)
            if (s1.intersection(s2)) != 0:
             x=x+1

   
print("колличество разделительных знаков: " ,(z))
print("колличество констант: " ,(b))
print("колличество заразервированных слов: " ,(x-1))
print("колличество символов: ",(s))




