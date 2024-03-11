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
				self.graph[v][u] += path_flow
				v = u

		return max_flow

	def min_cut(self, source, sink):
		visited = [False] * self.ROW
		self.dfs(source, sink, visited)

		min_cut_edges = []
		for i in range(self.ROW):
			for j in range(self.ROW):
				if visited[i] and not visited[j] and self.graph[i][j] > 0:
					min_cut_edges.append((i,j))

		return min_cut_edges

graph = [[0,16,13,0,0,0],
	 [0,0,10,12,0,0],
	[0,4,0,0,14,0],
	[0,0,9,0,0,20],
	[0,0,0,7,0,4],
	[0,0,0,0,0,0]]

g = Graph(graph)
source = 0
sink = 5
max_flow = g.ford_fulkerson(source, sink)
min_cut_edges = g.min_cut(source, sink)
print("The minimum cut edges:", min_cut_edges)
		
