# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
b=set(map(int,input().split()))
c=int(input())
d=set(map(int,input().split()))
print(len(b.symmetric_difference(d)))
