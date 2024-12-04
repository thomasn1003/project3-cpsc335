import heapq
from collections import defaultdict
from typing import List
 
def networkDelaytime(times: List[List[int]], n: int, k: int) -> int:
     #create the graph for adjacency list representation
     graph = defaultdict(list)
     for u, v, w in times:
         graph[u].append((v, w))  #append (neighbor, weight) to the adjacency list
 
     #min-heap to process nodes in increasing order of travel time
     pq = [(0, k)]  #start with source node `k` at time 0
 
     #dictionary to store the shortest time to each node
     dist = {}
 
     while pq:
         #pop the node with the smallest travel time
         time, node = heapq.heappop(pq)
 
         #continue if the node has already been processed
         if node in dist:
             continue
 
         #rcord the shortest time to the current node
         dist[node] = time
 
         #check neighbors if not already processed
         for neighbor, weight in graph[node]:
             if neighbor not in dist:
                 heapq.heappush(pq, (time + weight, neighbor))
 
     #check if all nodes are reachable
     if len(dist) < n:
         return -1
 
     #return the maximum travel time to reach all nodes
     return max(dist.values())

def main():
    #1     
     times1 = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
     print("Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2")
     print("Output: ", networkDelaytime(times1, 4, 2))
    #2 
     times2 = [[1, 2, 1]]
     print("Input: times = [[1,2,1]], n = 2, k = 1")
     print("Output: ", networkDelaytime(times2, 2, 1))
    #3 
     times3 = [[1, 2, 1]]
     print("Input: times = [[1,2,1]], n = 2, k = 2")
     print("Output: ", networkDelaytime(times3, 2, 2))
 
######## SAMPLE RUN ########
if __name__ == "__main__":
    main()

