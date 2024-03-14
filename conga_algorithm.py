import numpy as np

class CONGA:
	def __init__(self, adjacency_matrices):
		self.adjacency_matrices = adjacency_matrices
		self.num_snapshots = len(adjacency_matrices)
		self.num_nodes = adjacency_matrices[0].shape[0]

	def calculate_similarity(self, snapshot1, snapshot2):
		return np.sum(snapshot1 * snapshot2) / np.sqrt(np.sum(snapshot1) * np.sum(snapshot2))

	def aggregate_similarities(self):
		aggregated_similarities = np.zeros((self.num_nodes, self.num_nodes))
		for i in range(self.num_snapshots):
			for j in range(i+1, self.num_snapshots):
				similarity = self.calculate_similarity(self.adjacency_matrices[i], self.adjacency_matrices[j])
				aggregated_similarities += similarity
		return aggregated_similarities

	def find_communities(self):
		aggregated_similarities = self.aggregate_similarities()
		communities = []
		visited = set()
		for node in range(self.num_nodes):
			if node not in visited:
				community = [node]
				stack = [node]
				while stack:
					current_node = stack.pop()
					visited.add(current_node)
					neighbors = np.nonzero(aggregated_similarities[current_node])[0]
					for neighbor in neighbors:	
						stack.append(neighbor)
						community.append(neighbor)
				comminities.append(community)
		return communities


adjacency_matrices = [np.random.randint(0,2,size=(10,10)) for _ in range(5)]
conga = CONGA(adjacency_matrices)
communities = conga.find_communities()
print("Communities identified by CONGA:", communities)
