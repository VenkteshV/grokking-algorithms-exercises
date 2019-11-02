from collections import deque

def person_is_seller(name):
 return name[0] == "m"

def bfs_example():
    graph = {}
    graph["venky"] = ["datastruct","ml","algos", "mlbfs"]
    graph["algos"] = ["mlbfs"]
    graph["bfs"]=[]
    graph["datastruct"] = ["queues"]
    graph["ml"]=[]
    graph["queues"] =[]

    search_queue = deque()
    search_queue +=graph["venky"]
    isVisited = []
    while search_queue:
        person = search_queue.popleft()
        if not person in isVisited:
            if(person_is_seller(person)):
                print(person + " is a seller ")
                return True
            else :
                search_queue +=graph[person]
                isVisited.append(person)
    return False


bfs_example()