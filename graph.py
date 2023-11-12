from linked_lists import LinkedList
from stack import Stack
from queue import SimpleQueue

class Node():
    def __init__(self, label) -> None:
        self.label = label
        self.next = None


class Graph():
    def __init__(self) -> None:
        self.nodes = {}
        self.adjacency_list = {}

    def addNode(self, label):
        node = Node(label)
        if label not in self.nodes:
            self.nodes[label] = node
            self.adjacency_list[node] = []

    def removeNode(self, label):
        remove_node = self.nodes.get(label)

        if remove_node == None:
            return

        for node in list(self.adjacency_list.keys()):
            if remove_node in self.adjacency_list[node]:
                self.adjacency_list[node].remove(remove_node)

        self.adjacency_list.pop(remove_node)
        self.nodes.pop(label)

    def addEdge(self, from_label, to_label):
        from_node = self.nodes.get(from_label)
        to_node = self.nodes.get(to_label)

        if from_node == None or to_node == None:
            return "Illegal Argument"

        self.adjacency_list.get(from_node).append(to_node)


    def removeEdge(self, from_label, to_label):
        from_node = self.nodes.get(from_label)
        to_node = self.nodes.get(to_label)

        if from_node == None or to_node == None:
            return "Illegal Argument"

        self.adjacency_list[from_node].remove(to_node)


    def print(self):
        for source, connections in self.adjacency_list.items():
            if connections != []:
                labels = [c.label for c in connections]
                print(source.label + " is connected to " + ', '.join(labels))

    def traverseBF(self, root):
        node = self.nodes.get(root)
        if node== None:
            return

        queue = SimpleQueue()
        queue.put(node)

        visited = set()

        while (queue.empty() == False):
            current = queue.get()

            if current in visited:
                continue

            print(current.label)
            visited.add(current)

            for neighbor in self.adjacency_list.get(current):
                if neighbor not in visited:
                    queue.put(neighbor)

    
    def traverseDFR(self, root):
        node = self.nodes.get(root)
        if node== None:
            return

        stack = Stack()
        stack.push(node)

        visited = set()

        while (stack.isEmpty() == False):
            current = stack.pop()

            if current in visited:
                continue

            print(current.label)
            visited.add(current)

            for neighbor in self.adjacency_list.get(current):
                stack.push(neighbor)


    def traverseDF(self, root):
        node = self.nodes.get(root)
        if node== None:
            return

        self.traverse_nodes_df(node, set())

    def traverse_nodes_df(self, root, visited):
        print(root.label)
        visited.add(root)

        for node in self.adjacency_list.get(root):
            if node not in visited:
                self.traverse_nodes_df(node, visited)

    def topologicalSort(self):
        stack = Stack()
        visited = set()

        for node in list(self.nodes.values()):
            self.topo_sort(node, visited, stack)
        
        sorted = []
        while stack.isEmpty() == False:
            sorted.append(stack.pop().label)

        return sorted
 

    def topo_sort(self, node, visited, stack):
        
        if node in visited:
            return
        
        visited.add(node)

        for neighbor in self.adjacency_list.get(node):
            self.topo_sort(neighbor, visited, stack)

        stack.push(node)


    def hasCycle(self):
        all = set(self.nodes.values())
        visiting = set()
        visited  = set()

        while all != set():
            current = all.pop()
            if self.checkCycle(current, all, visiting, visited):
                return True

        return False

    def checkCycle(self, node : Node, all: set, visiting: set, visited: set):
        if node in all:
            all.remove(node)
        visiting.add(node)

        for neighbor in self.adjacency_list.get(node):

            if neighbor in visited:
                continue

            if neighbor in visiting:
                return True

            if self.checkCycle(neighbor, all, visiting, visited):
                return True
        
        visiting.remove(node)
        visited.add(node)


def main():
    graph = Graph()
    graph.addNode("A")
    graph.addNode("B")
    graph.addNode("C")
    graph.addEdge("A", "B")
    graph.addEdge("B", "C")
    graph.addEdge("C", "A")
    #print(graph.topologicalSort())
    print(graph.hasCycle())

if __name__ == "__main__":
    main()