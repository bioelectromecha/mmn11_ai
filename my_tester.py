import util


def shortestManhattanPathLength( positions ):

    if len(positions) <= 1:
        return 0

    explored = {positions[0]: 0 }
    frontier = util.PriorityQueue()
    frontier.push(positions[0], 0)
    path = {}

    while
        if frontier.isEmpty():
            raise Exception("no possible path exists")
        node = frontier.pop()
        if node in explored:
            continue
        explored[node] = 0
        if not positions:
            # goal found - return the path to it
            return sum(explored[vert] for vert in path)
        else:
            # added successor states to the frontier
            for successor in positions:
                print successor, cost, node
                if successor not in explored:
                    frontier.push(successor, cost + util.manhattanDistance(node, successor))
                    path[successor] = node


t0 = [(0,0),(0,2),(4,0),(4,2)] #8
t1 = [(0,0),(0,1),(1,0),(1,1)] #3
t2= [(0,0),(0,2),(2,0),(2,2),(1,1)] #8
t3 = [(0,1),(1,0),(1,2)] #4
t4 = [(0,0),(0,0),(2,2),(1,1),(2,2),(1,1)] #4
t5 = [(0,0),(0,1),(0,2),(3,0),(3,2)] #7
t6 = [(0,0),(3,0),(3,1),(3,2)]
t7 = [(1,0),(1,4),(0,2)] #6
t10 = [] #0
t11 = [(0,0)] #0

print shortestManhattanPathLength(t0)