import sys
import copy

input = lambda: sys.stdin.readline().strip()
"""
3<=n<=9로 n의 범위가 작기때문에 완전탐색으로 해결 가능
"""


def solve(arr, n):
    global op_list
    if len(arr) == n:
        op_list.append(copy.deepcopy(arr))
        return

    arr.append(" ")
    solve(arr, n)
    arr.pop()

    arr.append("+")
    solve(arr, n)
    arr.pop()

    arr.append("-")
    solve(arr, n)
    arr.pop()


t = int(input())
for _ in range(t):
    n = int(input())
    op_list = []
    solve([], n - 1)
    print(op_list)
    numbers = [i for i in range(1, n + 1)]
    print(numbers)
    for op in op_list:
        string = ""
        for i in range(n - 1):
            string += str(numbers[i]) + op[i]
        string += str(numbers[-1])
