# Surfing #
# December 08, 2019
# By Robin Nash


web = {}
visited = {}
w = int(input())

for i in range(w):
    line = site = input()
    
    # add site to web if it's not there
    if site not in web:
        web[site] = []

    visited[site] = False
        
    while line != "</HTML>":
        line = input()
        start = 0
        while line.find('<A HREF="',start) != -1:
            start = line.find('<A HREF="',start)
            end = line.find('">',start)
            if end != -1:
                url = line[start+9:end]
                web[site].append(url)
                visited[url] = False
                print("Link from",site,"to",url)
                start = end
            else:
                start += 9



while True:
    site = input()
    if site == "The End":
        break
    
    url = input()
    queue = web[site].copy()
    while queue != []:
        link = queue.pop()
        if not visited[link]:
            visited[link] = True
            if link in web:
                for w in web[link]:
                    queue.append(w)

    if visited[url]:
        print("Can",end =' ')
    else:
        print("Can't",end=' ')
    print("surf from",site,"to",url+".")
        
    for w in visited:
        visited[w] = False
    
                
            
        
#1575829336.0