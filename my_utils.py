
def getFarthestDistanceBetweenVertices( positions ):
    if len(positions) <= 1:
        return 0

    edgeList = []
    # add all edges and their cost to the list
    while positions:
        state = positions[0]
        del positions[0]
        # add all the edges from leading from the current state to all the other states
        edgeList.extend(map(lambda x: (util.manhattanDistance(state, x), state, x), positions))

    return max(edge[0] for edge in edgeList)

def calcShortestPathsLengthSum(positions):
    """ 
    :param positions: a list of positions (x,y) pacman should go reach
    :return: the sum of path lengths in a minimum spanning tree
    """
    # we use Kruskal's algorithm to calculate the minimum spanning tree
    # step 1) put all the edges and in the graph, with their cost, into a list of tuples (cost, vertice1, vertice2)

    if len(positions) <= 1:
        return 0

    edgeList = []
    # add all edges and their cost to the list
    while positions:
        state = positions[0]
        del positions[0]
        # add all the edges from leading from the current state to all the other states
        edgeList.extend(map(lambda x: (util.manhattanDistance(state, x), state, x), positions))

    # calculate a list of edges in a min spanning tree
    edgeList = calcMinSpanningTree(edgeList)

    # return the sum of edge costs in the MST
    return sum(edge[0] for edge in edgeList)


def calcMinSpanningTree(allEdgeList):
    """ calculate a minimum spanning tree list of edges via Kruskal's algorithm"""
    # remove all self referencing edges
    allEdgeList = filter(lambda z: z[0]!=0, allEdgeList)
    # sort the list of edges by their cost
    allEdgeList = sorted(allEdgeList)

    vertexSet = set()
    groupIdentifier = dict()
    identCounter = 0
    edgeList = []

    # build the minimum spanning tree - we rely on edgeList being sorted by cost
    for edge in allEdgeList:
        # add only edges connecting separate forests
        id1 = groupIdentifier.get(edge[1], -1)
        id2 = groupIdentifier.get(edge[2], -1)
        if id1 == id2 == -1:
            groupIdentifier[edge[1]] = identCounter
            groupIdentifier[edge[2]] = identCounter
            identCounter += 1
        elif id1 == id2:
            continue # they're in the same tree
        elif id1 == -1:
            groupIdentifier[edge[1]] = groupIdentifier[edge[2]]
        elif id2 == -1:
            groupIdentifier[edge[2]] = groupIdentifier[edge[1]]
        else:
            for vertex in vertexSet:
                if groupIdentifier[vertex] == id2:
                    groupIdentifier[vertex] = id1
        edgeList.append(edge)
        vertexSet.add(edge[1])
        vertexSet.add(edge[2])
    return edgeList