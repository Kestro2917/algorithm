class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[] for _ in range(vertices)]
		self.time = 0

	def addEdge(self, u, v):
		self.graph[u].append(v)
	
	def SCCUtil(self, u, low, disc, stackMember, st):
		disc[u] = self.time
		low[u] = self.time
		stackMember[u] = True
		st.append(u)

		for v in self.graph[u]:
			if disc[v] == -1:
				self.SCCUtil(v, low, disc, stackMember, st)
				low[u] = min(low[u], low[v])
			elif stackMember[v]:
				low[u] = min(low[u], disc[v])
		w = -1

		if low[u] == disc[u]:
			while w != u:
				w = st.pop()
				print(w, end=" ")
				stackMember[w] = False

	def SCC(self):
		disc = [-1] * self.V
		low = [-1] * self.V
		stackMember = [False] * self.V
		st = []
		
		for i in range(self.V):
			if disc[i] == -1:
				self.SCCUtil(i, low, disc, stackMember, st)

if __name__ == "__main__":
	g = Graph(5)
	g.addEdge(1, 0)
	g.addEdge(0, 2)
	g.addEdge(2, 1)
	g.addEdge(0, 3)
	g.addEdge(3, 4)

	print("Strongly Connected Components in the graph:")
	g.SCC()
