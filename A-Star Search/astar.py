# Initialization of Dictionaries
graph = {}                             
heuristics = {}                        

# Reading Input and Populating Dictionaries
f = open('input.txt', 'r')             
for line in f:                         
    node, heuristic, *neighbours = line.split()  
    heuristics[node] = int(heuristic)  
    graph[node] = {}                   
    for i in range(0, len(neighbours), 2):  
        neighbour = neighbours[i]      
        distance = int(neighbours[i+1]) 
        graph[node][neighbour] = distance 

# A* Search Algorithm 
def aStar(start, goal):               
    visited = {}                      
    for node in graph:                 
        visited[node] = False          
    distances = {}                     
    for node in graph:                 
        distances[node] = float('inf') 
    distances[start] = 0               
    queue = [(heuristics[start], 0, start, [])]  
    while queue:                       
        queue.sort()                   
        i, dist, node, path = queue.pop(0)  
        if visited[node]:             
            continue
        visited[node] = True           
        path = path + [node]          
        if node == goal:              
            return (path, dist)        
        for neighbour in graph[node]:  
            new_dist = dist + graph[node][neighbour]  
            if not visited[neighbour]: 
                queue.append((new_dist + heuristics[neighbour], new_dist, neighbour, path))  
                distances[neighbour] = min(distances[neighbour], new_dist)  # Update the distance to the neighbour in the distances dictionary
    return None                         # If goal node is not reachable, return None

# Main Function 
def main():                            
    start = input("Start node: ")      
    goal = input("Destination: ")     
    res = aStar(start, goal)          
