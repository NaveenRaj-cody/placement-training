# Enter your code here. Read input from STDIN. Print output to STDOUT
A=int(input())
c=set(map(int,input().split()))
B=int(input())
d=set(map(int,input().split()))
print(len(c.intersection(d)))
