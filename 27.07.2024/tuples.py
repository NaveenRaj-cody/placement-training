# Read input values
n = int(input())
integer_list = map(int, input().split())

# Create a tuple
t = tuple(integer_list)

# Calculate and print the hash value of the tuple
print(hash(t))
