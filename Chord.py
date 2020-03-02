from node import Node
import sys
import random

nodes = []
m = 8

def addNode():
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

def deleteNode(node):
	node.delete()
	nodes.remove(node)
	for n in nodes:
		for f in n.finger:
			f.node = f.node.findSuccessor(f.start)

def routeMessage(data):
	key = random.randint(0, 2**m - 1)
	random_node = random.choice(nodes)
	succ = random_node.findSuccessor(key)
	succ.hashTable[key] = data
	return key

for i in range(int(sys.argv[1])):
	addNode()

# for node in nodes:
# 	node.printNode()
def test1(nums):
	for i in range(5):
		random_node = random.choice(nodes)
		deleteNode(random_node)
	keys = []

	i = 0
	while(i < nums):
		key = routeMessage(i)
		if(key == None):
			print("Duplicate key")
		else:
			keys.append(key)
			i+=1

	# for i in range(nums):
	# key = chord.addMsg(i)
	# if(key == None):
	# print("Dupicate key")
	# i-=1
	# else:
	# keys.append(key)

	for i in range(nums):
		if(lookup(keys[i]) == i):
			print("Lookup: {} {} {}".format(keys[i], i, True))
			pass
		else:
			print("Lookup: {} {}".format(i, False))
			break

test1(10)