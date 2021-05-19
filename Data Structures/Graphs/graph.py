class Graph:
    def __init__ (self, edges, print_dict= False):
        self.edges = edges
        self.graph_dict = dict()
        #need to convert it to a better data structure: dictionary
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        if print_dict:
            print (self.graph_dict)
    
    
    #Finding all the routes between cities
    def get_paths(self, start, end, path= list()):
        path = path + [start]
        
        if start == end:
            return [path]

        if start not in self.graph_dict:
            return None
        
        paths = list()
        
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths
    
    #Finding the shortest path
    def shortest_path(self, start, end, path = list()):
        path = path + [start]
        
        if start == end:
            return path
        if start not in self.graph_dict:
            return None
        
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                shortest_so_far = self.shortest_path(node, end, path)
                if shortest_so_far:
                    if shortest_path is None or len(shortest_so_far) < len(shortest_path):
                        shortest_path = shortest_so_far
        return shortest_path
        


routes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto")
]


route_graph = Graph(routes)
start = "Mumbai"
end = "Toronto"
# print(route_graph.get_paths(start, end))
print(route_graph.shortest_path(start, end))


