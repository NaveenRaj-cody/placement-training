def average(array):
      array=set(array)
      avg=sum(array)/len(array)
      return avg
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
