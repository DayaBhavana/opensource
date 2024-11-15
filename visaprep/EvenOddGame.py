# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s=str(n)
a=0
for i in s:
    a+=int(i)
if a%2==0:
    print("Vignesh")
else:
    print("Charan")
    
