import sys
from linked_lists import LinkedList
from stack import Stack
from queue import SimpleQueue
from queue import PriorityQueue
from dataclasses import dataclass, field
from typing import Any

class Node():
    def __init__(self, label) -> None:
        self.label = label
        self.edges = []

    
    def addEdge(self, to_node, weight):
        self.edges.append(Edge(self, to_node, weight))

    def getEdges(self):
        return self.edges

class Path():
    def __init__(self):
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)

@dataclass(order=True)
class NodeEntry():
    weight : int
    node : Any=field(compare=False)


class Edge():
    def __init__(self, from_node, to_node, weight) -> None:
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    def getWeight(self):
        return self.weight

    def getToNode(self):
        return self.to_node


class WeightedGraph():
    def __init__(self) -> None:
        self.nodes = {}

    def addNode(self, label):

        if label not in self.nodes:
            self.nodes[label] = Node(label)


    def addEdge(self, from_label, to_label, weight):
        from_node = self.nodes.get(from_label)
        to_node = self.nodes.get(to_label)


        if from_node == None or to_node == None:
            return "Illegal Argument"

        from_node.addEdge(to_node, weight)
        to_node.addEdge(from_node, weight)

    def print(self):
        for node in list(self.nodes.values()):
            labels = [edge.getToNode().label for edge in node.getEdges()]
            print(f"{node.label} is connected to ", ', '.join(labels))

    def hasCycle(self):
        visited  = set()
        
        for node in list(self.nodes.values()):

            if node in visited:
                continue

            if self.checkCycle(node, None, visited):
                return True

        return False

    def checkCycle(self, node : Node, parent : Node, visited : set):

        visited.add(node)

        for edge in node.getEdges():
            if edge.to_node == parent:
                continue

            if edge.to_node in visited:
                return True

            if self.checkCycle(edge.to_node, node, visited):
                return True

        return False


    def getShortestPath(self, from_label, to_label):
        #Node : Integer(weight)
        distances = {}
        from_node = self.nodes.get(from_label)
        to_node = self.nodes.get(to_label)

        for node in list(self.nodes.values()):
            distances[node] = float('inf')

        distances[from_node] = 0
        visited = set()

        #Node : Node
        previous_nodes  = {}

        #use a priority queue    
        queue = PriorityQueue()
        queue.put(NodeEntry(0, from_node))
        
        while queue.empty() == False:
            current = queue.get().node
            visited.add(current)

            for edge in current.getEdges():

                if edge.to_node in visited:
                    continue

                new_distance = distances.get(current) + edge.weight

                if new_distance < distances.get(edge.to_node):
                    distances[edge.to_node] = new_distance
                    previous_nodes[edge.to_node] = current
                    queue.put(NodeEntry(new_distance, edge.to_node))


        stack = Stack()

        stack.push(to_node)
        previous = previous_nodes.get(to_node)
        while previous != None:
            stack.push(previous)
            previous = previous_nodes.get(previous)

        path = Path()
        while stack.isEmpty() == False:
            path.addNode(stack.pop().label)


        return path


    def getMinimumSpanningTree(self):
        tree = WeightedGraph()
        edges = PriorityQueue()

        start_node = self.nodes.values()[0]
        [edges.put((e.weight, e)) for e in start_node.getEdges()]

        tree.addNode(start_node.label)

        while len(tree.nodes) < len(self.nodes):
            min_edge = edges.get()
            next_node = min_edge.to_node

            if next_node.label in tree.nodes:
                continue

            tree.addNode(next_node.label)
            tree.addEdge(min_edge.from_node.label, next_node.label, min_edge.weight)

            for edge in next_node.getEdges():
                if edge.to_node.label not in tree.nodes:
                    edges.add(edge)


def main():
    graph = WeightedGraph()
    graph.addNode("A")
    graph.addNode("B")
    graph.addNode("C")
    graph.addEdge("A", "B", 1)
    graph.addEdge("B", "C", 2)
    graph.addEdge("A", "C", 10)
    path = graph.getShortestPath("A", "C")
    print_path = [n for n in path.nodes]
    print(" -> ".join(print_path))

if __name__ == "__main__":
    main()