n=int(input())
a=list(map(int,input().split()))
k=int(input())
k=k%n
r_a=a[-k:]+a[:-k]
print(*r_a)
