import networkx as nx

# Create a directed graph to represent the knowledge graph
kg = nx.DiGraph()

# Add nodes and edges (triplets: subject, predicate, object)
triplets = [
    ("Company", "has_metric", "Revenue"),
    ("Company", "CEO_of", "Person"),
    # Add more triplets from the knowledge extraction process
]

# Insert the triplets into the knowledge graph
for subj, pred, obj in triplets:
    kg.add_edge(subj, obj, label=pred)


# Function to perform depth-first search on the KG
def search_kg(query):
    relevant_subgraph = nx.dfs_edges(kg, source=query)
    return list(relevant_subgraph)
