import pydot

def write_graph(graph_dict, file_path):
    graph = pydot.Dot(graph_type="graph")
    for v1, neighbours in graph_dict.items():
        for v2 in neighbours:
            graph.add_edge(pydot.Edge(v1, v2))
    graph.write_png(file_path)