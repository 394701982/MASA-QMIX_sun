# from collections import defaultdict, deque
#
# # Step 1: 构建邻接表
# graph = defaultdict(list)
# graph[1] = [2,3,4,5,11,15]
# graph[2] = [6]
# graph[3] = [8]
# graph[4] = []
# graph[5] = [10]
# graph[6] = [7]
# graph[7] = []
# graph[8] = [9]
# graph[9] = []
# graph[10] = []
# graph[11] = [12]
# graph[12] = [13]
# graph[13] = [14]
# graph[14] = []
# graph[15] = [16]
# graph[16] = [17]
# graph[17] = []
#
#
#
#
# # Step 2: 计算每个节点的入度
# indegree = defaultdict(int)
# for node in graph:
#     for neighbor in graph[node]:
#         indegree[neighbor] += 1
#
# # 初始化所有节点的入度为0
# all_nodes = set(graph.keys()).union({n for neighbors in graph.values() for n in neighbors})
# for node in all_nodes:
#     indegree[node] = indegree.get(node, 0)
#
# # Step 3: 找出入度为0的节点
# queue = deque([node for node in all_nodes if indegree[node] == 0])
#
# print(f"初始入度为0的节点: {list(queue)}")
#
# # Step 4: 选取入度为0的节点，并删除该节点，更新其他节点的入度
# while queue:
#     current = queue.popleft()
#     print(f"选择节点: {current}")
#
#     # 更新该节点的所有后继节点的入度
#     for neighbor in graph[current]:
#         indegree[neighbor] -= 1
#         if indegree[neighbor] == 0:
#             queue.append(neighbor)
#
#     # 打印当前入度为0的节点
#     print(f"当前入度为0的节点: {list(queue)}")


from collections import defaultdict, deque

# Step 1: 构建邻接表
graph = defaultdict(list)
graph[5] = [4,2,3]
graph[2] = [6]
graph[3] = [7]
graph[4] = [8]
graph[1] = [0]
graph[6] = [0]
graph[7] = [0]
graph[8] = [1]
# graph[9] = []
# graph[10] = []
# graph[11] = [12]
# graph[12] = [13]
# graph[13] = [14]
# graph[14] = []
# graph[15] = [16]
# graph[16] = [17]
# graph[17] = []

# Step 2: 计算每个节点的入度
indegree = defaultdict(int)
for node in graph:
    for neighbor in graph[node]:
        indegree[neighbor] += 1

# 初始化所有节点的入度为0
all_nodes = set(graph.keys()).union({n for neighbors in graph.values() for n in neighbors})
for node in all_nodes:
    indegree[node] = indegree.get(node, 0)

# Step 3: 找出入度为0的节点
queue = deque([node for node in all_nodes if indegree[node] == 0])

# 未执行的节点集合
unexecuted_nodes = set(all_nodes)

print(f"初始入度为0的节点: {list(queue)}")

# Step 4: 选取入度为0的节点，并删除该节点，更新其他节点的入度
while queue:
    current = queue.popleft()
    unexecuted_nodes.remove(current)  # 从未执行的节点中移除

    print(f"选择节点: {current}")
    print(f"未执行的节点: {sorted(unexecuted_nodes)}")

    # 更新该节点的所有后继节点的入度
    for neighbor in graph[current]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            queue.append(neighbor)

    # 打印当前入度为0的节点
    print(f"当前入度为0的节点: {list(queue)}")

