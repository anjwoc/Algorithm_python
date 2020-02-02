import sys
import heapq
input = lambda: sys.stdin.readline().strip()

k, n = map(int, input().split())
arr = []
heap = []
pr = 0
# 수가 중복으로 들어올 수 있는데 중복으로 들어오면
# 들어온만큼 이용해야한다.
for _ in range(k):
  tmp = input()
  print(type(tmp))
  arr.append((int(tmp[0]), tmp)
  # print(tmp[0])
  # first = int(tmp[0])
  heapq.heappush(heap, (-first, tmp))

for _ in range(len(heap)):
  if len(heap)>=0:
    print(heapq.heappop(heap)[1], end='')
  else:
    # 숫자들을 1번 이상 사용할 경우
    print(type(arr))
    print(type(arr[1]))
    