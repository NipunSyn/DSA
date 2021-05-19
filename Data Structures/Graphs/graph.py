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
    def get_paths(self, start, end, path= []):
        path += [start]
        
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
end = "New York"
print(route_graph.get_paths(start, end))



#Finding the shortest path