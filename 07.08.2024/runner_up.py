if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    s=list(set(arr))
    m=max(s)
    for i in s:
        if m in s:
            s.remove(m)
    print(max(s))
