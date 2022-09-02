import queue as q
from RMP import dict_gn
def bfs(current_city, goal_city, explored_list, exploration_queue):
    explored_list.append(current_city)
    goal_reached = False
    if current_city == goal_city:
         return explored_list, True
    for each_city in dict_gn[current_city].keys():
        if each_city not in explored_list and each_city not in exploration_queue.queue:
             exploration_queue.put(each_city)
    try:
         explored_list, goal_reached = bfs(exploration_queue.get(False), goal_city, explored_list, exploration_queue)
    except q.Empty:
        return explored_list, False
    if goal_reached:
        return explored_list, True
    return explored_list, False
def main():
    start_city = 'Arad'
    goal_city = 'Bucharest'
    explored_list = []
    exploration_queue = q.Queue()
    exploration_queue.put(start_city)
    goal_reached = False
    explored_list, goal_reached = bfs(exploration_queue.get(False),goal_city, explored_list, exploration_queue)
    if not goal_reached:
         print('Could not find', goal_city)
    print(explored_list) 
main()            
         

"""
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


print("Following is the Breadth-First Search")
bfs(visited, graph, '5')    # function calling

"""
