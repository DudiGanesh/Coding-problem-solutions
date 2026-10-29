if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_set=set(arr)
    unique_set.remove(max(unique_set))
    print(max(unique_set))
