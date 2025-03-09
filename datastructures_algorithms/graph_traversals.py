#!/usr/bin/env/python

# from http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

from Graphs import Graph

def depth_first_search(graph, start_node):
	""" Performs depth first search. """

	# visited nodes are stored in a list instead of set so order matters 
	# WHEN PRINTING
	visited = []
	
	# stack to keep track of which vertices next
	stack = [start_node]

	# while the stack isnt empty keep going
	while len(stack) != 0:
		# pop the top node, if has been visited before, do nothing
		vertex = stack.pop()

		# if it hasnt been visited, add it on to the list of visited.
		if vertex not in visited:
			visited.append(vertex)

			# push on all the vertices that are reachable from this vertex and havent
			# been visited yet.
			stack.extend(graph[vertex] - set(visited))
	
	return visited



def breath_first_search(graph, start_node):
	""" Performs breath first search. """

	# visited nodes are stored in a list instead of set so order matters
	visited = []
	
	# queue to keep track of which vertices next
	queue = [start_node]

	# while the queue isnt empty keep going
	while len(queue) != 0:

		# pop from the front of the queue, if has been visited before, do nothing
		vertex = queue.pop(0)

		# if it hasnt been visited, add it on to the back of the queue
		if vertex not in visited:
			visited.append(vertex)

			# push all the vertices that are reachable from this vertex and havent
			# been visited yet on to the back of the queue.
			queue.extend(graph[vertex] - set(visited))
	
	return visited



if __name__ == "__main__":

	connections = [('A','B'), ('A', 'C'), ('B','D'),
								 ('B','E'), ('E', 'F')] #, ('C','F')]

	g = Graph(connections, directed=True)

	print g

	print "DFS"
	print depth_first_search(g, 'A')

	print "BFS"
	print breath_first_search(g, 'A')


	



