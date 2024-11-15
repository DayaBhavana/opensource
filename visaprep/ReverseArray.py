# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
arr=list(map(int,input().split()))
a=arr[::-1]
print(*a)
