arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

# 정석
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#     def insert(self, child):
#         if not self.left:
#             self.left = child
#             return
#         if not self.right:
#             self.right = child
#             return
#         return
#     def inorder(self):
#         if self != None:
#             if self.left:
#                 self.left.inorder()
#             print(self.value, end=' ')
#             if self.right:
#                 self.right.inorder()
#
# nodes = [TreeNode(i) for i in range(0, 14)]
#
# for i in range(0, len(arr), 2):
#     parent_node = arr[i]
#     child_node = arr[i+1]
#     nodes[parent_node].insert(nodes[child_node])
#
# nodes[1].inorder()

# 코테용
nodes = [[] for _ in range(14)]
for i in range(0, len(arr), 2):
    parent_node = arr[i]
    child_node = arr[i+1]
    nodes[parent_node].append(child_node)

for li in nodes:
    for _ in range(len(li), 2):
        li.append(None)

def inorder(nodeNum):
    if nodeNum == None:
        return
    inorder(nodes[nodeNum][0])
    print(nodeNum, end=' ')
    inorder(nodes[nodeNum][1])

inorder(1)