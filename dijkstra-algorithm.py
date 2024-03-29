def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def dijkstra():
    graph = {}
    graph["venktesh"] = ["aswath","kavi","muthu"]
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2
    graph["a"] = {}
    graph["a"]["finish"] = 1
    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["finish"] = 5
    graph["finish"] = {}
    infinity = float("inf")
    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["finish"] = infinity
    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["finish"] = None
    processed = []
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for n in neighbours.keys():
            new_cost = cost + neighbours[n]
            if(costs[n] > new_cost):
                costs[n]  = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    print(parents)
    print(costs)

dijkstra()