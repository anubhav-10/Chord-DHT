from node import Node
import sys
import random

nodes = []

def add_node():
	new_node = Node(8)
	if len(nodes) != 0:
		random_node = random.choice(nodes)
		new_node.join(random_node)
	nodes.append(new_node)

def lookup(key):
	random_node = random.choice(nodes)
	succ = random_node.findSuccessor(key)
	if key in succ.hashTable:
		return succ.hashTable[key]
	return None

def routeMessage(key, data):
	random_node = random.choice(nodes)
	succ = random_node.findSuccessor(key)
	succ.hashTable[key] = data

for i in range(int(sys.argv[1])):
	add_node()

for node in nodes:
	node.printNode()