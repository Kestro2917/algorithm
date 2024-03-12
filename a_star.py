import heapq

class Graph:
	def __init__(self):
		self.adj_list = {}

	def add_edge(self, u, v, weight):
		if u not in self.adj_list:
			self.adj_list[u] = []
		self.adj_list[u].append((v, weight))

	def astar_search(self, start, goal):
		open_set = [(0, start)]
		came_from = {}
		g_score = {node: float('inf') for node in self.adj_list}
		g_score[start] = 0
		f_score = {node: float('inf') for node in self.adj_list}
		f_score[start] = self.heuristic(start, goal)

		while open_set:
			_, current = heapq.heappop(open_set)
			if current == goal:
				return self.reconstruct_path(came_from, current)
			for neighbor, weight in self.adj_list[current]:
				tentative_g_score = g_score[current] + weight
				if tentative_g_score < g_score.get(neighbor, float('inf')):
					came_from[neighbor] = current
					g_score[neighbor] = tentative_g_score
					f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
					heapq.heappush(open_set, (f_score[neighbor], neighbor))

		return None


	def heuristic(self, node, goal):
		return ((node[0] - goal[0]) ** 2 + (node[1] - goal[1]) ** 2) ** 0.5

	def reconstruct_path(self, came_from, current):
		path = [current]
		while current in came_from:
			current = came_from[current]
			path.append(current)
		return list(reversed(path))

graph = Graph()
graph.add_edge((0,0), (0,1), 1)
graph.add_edge((0,0), (1,0), 1)
graph.add_edge((0,1), (1,1), 1)
graph.add_edge((1,0), (1,1), 1)

start = (0,0)
goal = (1,1)
path = graph.astar_search(start, goal)
print("Shortest path from", start, "to", goal, ":", path)
