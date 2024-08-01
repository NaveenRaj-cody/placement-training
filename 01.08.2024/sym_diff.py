# Enter your code here. Read input from STDIN. Print output to STDOUT
M=int(input())
a=set(list(map(int,input().split())))
N=int(input())
b=set(list(map(int,input().split())))
c=a.symmetric_difference(b)
d=sorted(c)
for i in c:
    print(i)
