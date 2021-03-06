import sys
input = lambda: sys.stdin.readline().strip()

t = int(input())
form = []
for _ in range(t):
  n, m = map(int, input().split())
  books = list(range(n+1))
  check = [False] * (1001)
  for _ in range(m):
    ai, bi = map(int, input().split())
    form.append((ai, bi))
  ans = 0
  
  form.sort(reverse = True) # 이거 잘못됌 lambda로 키 지정해야된다.

  for i in range(m):
    for j in range(1, n+1, 1):
      if not check[j] and form[i][0] <= j and j <= form[i][1]:
        check[j] = True
        ans += 1
        break

  print(ans)
