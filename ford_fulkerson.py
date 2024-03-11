class Graph:
	def __init__(self, graph):
		self.graph = graph
		self.ROW = len(graph)

	def dfs(self, s, t, parent):
		visited = [False] * self.ROW
		stack = [(s, float('inf'))]
		visited[s] = True

		while stack:
			u, flow = stack.pop()
			for ind, val in enumerate(self.graph[u]):
				if not visited[ind] and val > 0:
					stack.append((ind, min(flow, self.graph[u][ind])))
					visited[ind] = True
					parent[ind] = u
					if ind == t:
						return True, flow
		return False, 0

	def ford_fulkerson(self, source, sink):
		parent = [-1] * self.ROW
		max_flow = 0
		
		while True:
			found_augmenting_path, path_flow = self.dfs(source, sink, parent)
			if not found_augmenting_path:
				break
			max_flow += path_flow
			v = sink
			while v != source:
				u = parent[v]
				self.graph[u][v] -= path_flow
				self.graph[u][v] += path_flow
				v = u

			return max_flow

# Example usage:

graph = [[0,16,13,0,0,0],
	[0,0,10,12,0,0],
	[0,4,0,0,14,0],
	[0,0,9,0,0,20],
	[0,0,0,7,0,4],
	[0,0,0,0,0,0]]

g = Graph(graph)
source = 0
sink = 5
print("The maximum possible flow is:", g.ford_fulkerson(source, sink))
