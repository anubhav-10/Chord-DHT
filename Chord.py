from node import Node
import sys
import random
from collections import Counter

nodes = []
keys = []
m = 32

def addNode():
	new_node = Node(m)
	if len(nodes) != 0:
		random_node = random.choice(nodes)
		new_node.join(random_node)
	nodes.append(new_node)

def lookup(key):
	random_node = random.choice(nodes)
	hops = []
	succ = random_node.findSuccessor(key, hops)
	if key not in succ.hashTable:
		return None, hops
	return succ.hashTable[key], hops

def deleteNode(node):
	node.delete()
	nodes.remove(node)
	for n in nodes:
		for f in n.finger:
			f.node = f.node.findSuccessor(f.start, [])

def routeMessage(data = None):
	key = random.randint(0, 2**m - 1)
	random_node = random.choice(nodes)
	succ = random_node.findSuccessor(key, [])
	if data == None:
		data = hex(random.randint(0, 2**(32) - 1))[2:]
	succ.hashTable[key] = data
	keys.append(key)
	return key

def route_multiple_msg(num):
	for i in range(num):
		routeMessage()

def remove_random_node():
	random_node = random.choice(nodes)
	deleteNode(random_node)

def add_multiple_nodes(num):
	for i in range(num):
		addNode()

def remove_multiple_nodes(num):
	for i in range(num):
		remove_random_node()
		print ("Deleted: " + str(i))

def print_hops(hops, key):
	print ('Look up for ' + str(key) + ':', end = ' ')
	for i in hops:
		print (i, end = ' -> ')

	print()

