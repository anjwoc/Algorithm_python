import sys
input = lambda: sys.stdin.readline().strip()

class Node:
    def __init__(self, number, left_node, right_node):
        self.parent = -1
        self.left_node = left_node
        self.right_node = right_node

def in_order(node, level):
    global level_depth, x
    level_depth = max(level_depth, x)
    if node.left_node != -1:
        in_order(tree[node.left_node], level+1)
    # 방문했을 때의 x좌표 값과 비교해서 변경
    level_min[level] = min(level_min[level], x)
    level_max[level] = max(level_max[level], x)
    x += 1
    if node.right_node != -1:
        in_order(tree[node.right_node], level+1)

n = int(input())
tree = {}
level_min = [n]
level_max = [0]
root = -1 # 루트 노드의 인덱스
x = 1 # x 좌표
level_depth = 1 # 전체 트리의 뎁스를 기록하기 위함

for i in range(1, n+1):
    tree[i] = Node(i, -1, -1)
    level_min.append(n)
    level_max.append(0)

for _ in range(n):
    number, left_node, right_node = map(int, input().split())
    tree[number].left_node = left_node
    tree[number].right_node = right_node
    if left_node != -1:
        tree[left_node].parent = number
    if right_node != -1:
        tree[right_node].parent = number
    
for i in range(1, n + 1):
    if tree[i].parent == -1:
        root = i

in_order(tree[root], 1)
print(level_min)
print(level_max)

result_level = 1
result_width = level_max[1] - level_min[1] + 1
for i in range(2, level_depth + 1):
    width = level_max[i] - level_min[i] + 1
    if result_width < width:
        result_level = i
        result_width = width
print(result_level, result_width)
