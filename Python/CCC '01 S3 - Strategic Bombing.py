# Strategic Bombing #
# February 17, 2019
# By Robin Nash

#used to convert letters to a number 0-25
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#make a 2D list of 26 empty lists as there are a maximum of 26 letters and any letter can be chosen
graph = [[] for i in range (26)]

#will store each edge
edges = []


while True:
    edge = input()
    if edge == "**":
        break
    
    #convert letter edge to tuple -> ex "AC" -> (0,2)
    a,b = (alpha.find(ch) for ch in edge)
    
    #add edge to edges
    edges.append((a,b))
    
    #add the second node to the first node's list of connected nodes
    graph[a].append(b)
    
    #and vise versa
    graph[b].append(a)

#stores the edges that disconnect A to B
answers = []

for a,b in edges:
    #Remove the edge by removing b from a's list of connected nodes and vise versa
    graph[a].remove(b)
    graph[b].remove(a)
    
    vis = [False for i in range(26)]
    queue = [0]
    vis[0] = True

    while queue != []:

        node = queue.pop(0)

        for n in graph[node]:
            if not vis[n]:
                queue.append(n)
                vis[n] = True
                
    if not vis[1]:
        answers.append(alpha[a]+alpha[b])

    graph[a].append(b)
    graph[b].append(a)

for edge in answers:
    print(edge)

print("There are",len(answers) ,"disconnecting roads.")


#1550377410.0
