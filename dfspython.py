graph ={}
num_node = int(input("enter the number of nodes :"))
for _ in range(num_node):
    node =input("enter the node:")
    neighbours = input("enter the neighbours of {node} separated by spaces(leave empty if none):").split()
    graph[node] = neighbours
visited = set()
def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbours in graph[node]:
            dfs(visited,graph,neighbours)
start_node =input(" enter the start node of dfs:")
print("following is the depth first search :")
dfs(visited,graph,start_node)
