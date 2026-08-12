from heapq import heappush, heappop

def qheap():
    arr = []
    active_set = set()

    n = int(input())
    for i in range(n):
        T = list(map(int, input().split()))
        if T[0] == 1:
            heappush(arr, T[1])
            active_set.add(T[1])
        elif T[0] == 2:
            active_set.discard(T[1])
        else:
            while arr[0] not in active_set:
                heappop(arr)
            print(arr[0])

qheap()