import random

class Finger:
	def __init__(self, n, m, i, node = None):
		self.start = (n + 2**(i)) % (2**m)
		self.end = (n + 2**(i-1) - 1) % (2**m)
		self.node = node

class Node:
	def __init__(self, m = 16):
		self.m = m
		self.M = 2 ** m
		self.successor = self
		self.predecessor = self
		self.key = random.randint(0, 2**m - 1)
		self.finger = [Finger(self.key, m, i, self) for i in range(m)]
		self.hashTable = {}

	def join(self, node):
		self.initializeFingerTable(node)
		self.updateOthers()

	def initializeFingerTable(self, node):
		self.finger[0].node = node.findSuccessor(self.key, [])
		self.successor = self.finger[0].node
		self.predecessor = self.successor.predecessor
		self.successor.predecessor = self
		self.predecessor.successor = self

		for i in range(1, self.m):
			# if self.finger[i].start == self.successor.key:
			# 	self.finger[i].node = self.successor
			if self.finger[i].start == self.successor.key or self.inBetween(self.finger[i].start, self.key, self.successor.key):
				self.finger[i].node = self.successor
			else:
				self.finger[i].node = node.findSuccessor(self.finger[i].start, [])

	def updateOthers(self):
		for i in range(self.m):
			temp = (self.key - 2 ** (i)) % self.M
			pred = self.findSuccessor(temp, [])
			# pred = self.findPredecessor(self.key - 2 ** (i))
			if pred.key != temp:
				pred = pred.predecessor
			pred.updateFingerTable(self, i)

	def updateFingerTable(self, node, i):
		if self.inBetween(node.key, self.key, self.finger[i].node.key):
			self.finger[i].node = node
			p = self.predecessor
			p.updateFingerTable(node, i)

	def findSuccessor(self, key, hops):
		if (self.key == key):
			return self
		# elif (self.successor.key == key):
		# 	return self.successor
		elif self.successor.key == key or self.inBetween(key, self.key, self.successor.key):
			return self.successor
		else:
			hops.append(self.key)
			return self.closestPreceedingFinger(key, hops)

	def closestPreceedingFinger(self, key, hops):
		for i in range(self.m - 1, -1, -1):
			if self.inBetween(self.finger[i].node.key, self.key, key):
				return self.finger[i].node.findSuccessor(key, hops)

		return self

	# check if n is in between a and b
	def inBetween(self, n, a, b):
		if (b > a):
			return a < n < b

		b += self.M
		if a > n:
			n += self.M
		return a < n < b

	def delete(self):
		self.predecessor.successor = self.successor
		self.successor.predecessor = self.predecessor

	def printFingerTable(self):
		for finger in self.finger:
			print (finger.start, finger.node.key)

	def printNode(self):
		print("||| --- Printing for node: {} --- |||".format(self.key))
		print("[@] Successor: {}".format(self.successor.key))
		print("[@] Predecessor: {}".format(self.predecessor.key))
		print()
		print("[@] Fingertable")
		self.printFingerTable()
		print("||| --- --- --- --- --- --- --- --- --- |||")
		print()
		print()
