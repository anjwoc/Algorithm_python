import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
cnt = 1
st = []
ans = []

for i in range(1, n + 1):  # data lenght만큼 반복
    data = int(input())
    while cnt <= data:
        st.append(cnt)
        cnt += 1
        ans.append("+")
    if st[-1] == data:
        st.pop()
        ans.append("-")
    else:
        print("NO")
        exit(0)
print("\n".join(ans))

