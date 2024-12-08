# """
# 这个文件用于描述task的内容
#
# """
# from utils.job import Jobs
#
# class Task:
#     def __init__(self):
#         # 当前仅考虑最简单的任务，串行任务
#         self.simple_task = [5, 4, 2, 3, 8, 6, 7, 1, 0]  # 时间最快是74完成
#         jobs = Jobs()
#         # 带有对象的
#         self.simple_task_object = []
#         for eve in self.simple_task:
#             self.simple_task_object.append(jobs.jobs_object_list[eve])
#


from collections import defaultdict, deque
from utils.job import Jobs


class Task:
    def __init__(self):
        # 当前仅考虑最简单的任务，串行任务

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



        jobs = Jobs()
        # 带有对象的
        self.simple_task_object = []
        self.simple_task_object=all_nodes
