n=153
sum=0
t=n
while(t>0):
    d=t%10
    sum +=d**3
    n=n//10

if(sum==t):
    print("Armstrong")