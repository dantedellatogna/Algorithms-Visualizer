# Definition of the dictionaries that contain the graphs
graph = {
    '0': ['1', '2', '3'],
    '1': ['0', '2'],
    '2': ['0', '1', '4'],
    '3': ['0'],
    '4': ['2']
}

graph2 = {
    '2': ['0', '1', '4'],
    '3': ['0'],
    '1': ['0', '2'],
    '4': ['2'],
    '0': ['1', '2', '3'],

}


graph3 = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': [],
    '4': [],
    '5': []
}


graph4 = {
    '1': ['2', '3', '4', '5'],
    '2': ['1', '6'],
    '3': ['1', '6'],
    '4': ['1', '7'],
    '5': ['1', '7'],
    '6': ['2', '3', '8'],
    '7': ['4', '5', '8'],
    '8': ['6', '7']
}


visited = []  # Contains the nodes that have been already visited.
# Contains the adjacent nodes of the current node. It's re-ordered with every new node visited.
stack = []


# Main program
def DFS(start):

    # Every time a node is visited for the first time, it's added to the "visited" list.
    visited.append(start)

    # If "start" is in the "stack" list, we remove it from the list.
    if start in stack:
        stack.pop(stack.index(start))

    for i in reversed(graph4[start]):
        if i not in visited:
            if i in stack:
                stack.pop(stack.index(i))
            stack.insert(0, i)

    print(f'visited: {visited}')
    print(f'stack: {stack}\n')
    for i in stack:
        if i not in visited:
            DFS(i)


# Main run
def run():
    start = '1'
    DFS(start)


# Test run
def run2():
    for keys, values in graph3.items():
        if values:
            print(keys)
            print(values)


if __name__ == '__main__':
    run()
