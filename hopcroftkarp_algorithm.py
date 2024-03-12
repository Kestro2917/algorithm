class HopcroftKarp:
	def __init__(self, graph):
		self.graph = graph
		self.matching = {}
		self.dist = {}
		self.nil = 0
		self.N = len(graph)
		self.INF = float('inf')
		
	def bfs(self):
		for u in range(1, self.N + 1):
			if self.matching.get(u, None) is None:
				self.dist[u] = 0
			else:
				self.dist[u] = self.INF
		self.dist[self.nil] = self.INF
		queue = [self.nil]
		while queue:
			u = queue.pop(0)
			if u != self.nil:
				for v in self.graph[u]:
					if self.dist[self.matching[v]] == self.INF:
						self.dist[self.matching[v]] = self.dist[u] + 1
						queue.append(self.matching[v])
		return self.dist[self.nil] != self.INF

	def dfs(self, u):
		if u != self.nil:
			for v in self.graph[u]:
				if self.dist[self.matching[v]] == self.dist[u] + 1:
					if self.dfs(self.matching[v]):
						self.matching[v] = u
						self.matching[u] = v
						return True
			self.dist[u] = self.INF
			return False
		return True

	def hopcroft_karp(self):
		matching = 0
		while self.bfs():
			for u in range(1, self.N + 1):
				if self.matching.get(u, None) is None:
					if self.dfs(u):
						matching += 1
		return matching

graph = {
	1: [6],
	2: [6, 7],
	3: [7],
	4: [7],
	5: [8],
	6: [1, 2],
	7: [2, 3, 4],
	8: [5]
}

hk = HopcroftKarp(graph)
max_matching = hk.hopcroft_karp()
print("Maximum cardinality matching:", max_matching)

			

		
