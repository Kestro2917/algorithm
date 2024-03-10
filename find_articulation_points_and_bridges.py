from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
		self.visited = {}
		self.disc = {}
		self.low = {}
		self.parent = {}
		self.time = 0
		self.articulation_points = set()
		self.bridges = set()

	def add_edge(self, u, v):
		self.graph[u].append(v)	
		self.graph[v].append(u)

	def dfs(self, u):
		self.visited[u] = True
		self.disc[u] = self.time
		self.low[u] = self.time
		self.time += 1
		children = 0

		for v in self.graph[u]:
			if v not in self.visited:
				children += 1
				self.parent[v] = u
				self.dfs(v)

				self.low[u] = min(self.low[u], self.low[v])
				
				if self.parent[u] is None and children > 1:
					self.articulation_points.add(u)
				elif self.parent[u] is not None and self.low[v] >= self.disc[u]:
					self.articulation_points.add(u)

				if self.low[v] > self.disc[u]:
					self.bridges.add((u,v))

			elif v != self.parent[u]:
				self.low[u] = min(self.low[u], self.disc[v])

	
	def find_articulation_points_and_bridges(self):
		self.time = 0
		for u in self.graph:
			if not self.visited.get(u, False):
				self.parent[u] = None
				self.dfs(u)

		return self.articulation_points, self.bridges

g  = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(2, 5)

articulation_points, bridges = g.find_articulation_points_and_bridges()

print("Articulation Points:", articulation_points)
print("Bridges:", bridges)
