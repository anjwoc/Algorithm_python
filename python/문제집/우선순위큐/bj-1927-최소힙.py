import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    data = int(input())
    if data != 0:
        heapq.heappush(heap, data)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
