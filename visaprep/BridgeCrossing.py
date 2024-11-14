# Enter your code here. Read input from STDIN. Print output to STDOUT
x=int(input())
d1=int(x*0.1)
d2=100
r=max(d1,d2)
if r==d1:
    print(x-d1)
else:
    print(x-d2)
