graph={}
num_node=int(input("enter the number of node in dfs :"))
for _ in range(num_node):
    node=input("enter the node :")
    n=input("enter the neighbour of {node} :")
    graph[node]=n
visited=set()
def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for n in graph[node]:
            dfs(visited,graph,n)
start_node=input("start with :")
dfs(visited,graph,start_node)