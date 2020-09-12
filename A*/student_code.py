from queue import PriorityQueue
from math import sqrt
    
def heuristic(x, y):
    return sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)

def generate_path(prev, start, goal):
    cur = goal
    get_path = [cur]
    while cur != start:
        cur = prev[cur]
        get_path.append(cur)
    get_path.reverse()
    return get_path

def shortest_path(map_40,start,goal):
    frontier = PriorityQueue()
    frontier.put(start, 0) 
    prev = {start: None}
    cost_1 = {start: 0}
    visited = set()
    while not frontier.empty():
        cur = frontier.get()
        #print(cur)
        visited.add(cur)
        if cur == goal:
            generate_path(prev, start, goal)    
        for node in map_40.roads[cur]:
            if node not in visited:
                pass
            cost_2 = cost_1[cur]+heuristic(map_40.intersections[cur], map_40.intersections[node])
            if node not in cost_1 or cost_2 < cost_1[node]:
                cost_1[node] = cost_2
                func = cost_2 + heuristic(map_40.intersections[goal], map_40.intersections[node])
                frontier.put(node, func)
                prev[node] = cur

    return generate_path(prev, start, goal)