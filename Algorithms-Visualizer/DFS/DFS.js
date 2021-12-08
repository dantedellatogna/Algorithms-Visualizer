var visited = []
var stack = []

class Node {
    constructor(value, adj){
        this.value = value
        this.adj = adj
    }
}

function DFS(start) {
    // Every time a node is visited for the first time, it's added to the "visited" list.
    visited.push(start)

    let node = new Node(start, start.adj) // How do I initialize the adj nodes?

    // If "start" is in the "stack" list, we remove it from the list.
    if (stack.length > 0) {
        for (let i = 0; i < stack.length; i++) {
            if (start == stack[i]) {
                stack.splice(i, 1)
            }
        }
    }
    
    // Here I'll add the adj nodes of "start" to the "stack" array.
    for (let i = 0; i < array.length; i++) {
        const element = array[i];
        
    }
}