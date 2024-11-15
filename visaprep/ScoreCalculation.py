# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    print(x//10*y)
