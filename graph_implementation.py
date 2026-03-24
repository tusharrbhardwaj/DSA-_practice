# grap and working with depth first traversing algorithm

#code through iteration

# def depthfirstPrint(graph, source):
#     stack = [source]
    
#     while len(stack) != 0:
#         current = stack.pop()
#         print(current)
#         for eachn in graph[current]:
#             stack.append(eachn)
    

#code through recurssion

def depthfirstPrint(graph, source):
    print(source)
    
    for eachn in graph[source]:
        depthfirstPrint(graph, eachn)



graph = {
    'a' : ['b','c' ],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : []
}


depthfirstPrint(graph, 'a') # ---> acebdf