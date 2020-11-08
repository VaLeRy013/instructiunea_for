n=int(input("dati n: "))
x=1
s=0
s2=0
s3=0
pr=1
div=0
s4=0
s5=3
for x in range(1, n+1):
    s=s+x
print(s)
n=int(input("dati n: "))
for x in range(1, n+1):
   s2=((x-1)*x)+s2
print(s2)
n=int(input("dati n: "))
for x in range(1, n+1):
    pr*=x
    s3+=pr
print(s3)
s3=0
n=int(input("dati n: "))
for x in range(1, n+1):
   x=str(x)
   x=int(x+"2")
   s3=x+s3
print(s3)
n=int(input("dati n: "))
for x in range(1, n+1):
    div=x/(x+1)
    s4=div+s4
print(s4)
n=int(input("dati n: "))
for x in range(3, n+1):
    x=str(x)
    x=int("2"+x)
    s5=s5+x
print(s5)