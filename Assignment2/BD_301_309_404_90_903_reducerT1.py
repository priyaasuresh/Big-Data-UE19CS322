#!/usr/bin/python3

import sys

file_path=sys.argv[1]
node_under_processing = None
fromNode = None
v_file=open(file_path,'w')
l=[]
for line in sys.stdin:
	fromNode, toNode = line.split()
	if (node_under_processing == None):
		node_under_processing = fromNode
		print(fromNode,end=' ')
		l.append(int(toNode))
		print(fromNode,', 1',sep='',file=v_file)
		#node_under_processing = fromNode

	elif fromNode == node_under_processing:
		l.append(int(toNode))

	else:
		if node_under_processing:
			l.sort()
			#print(" ".join(l))
			print(" ",l)
			l=[]
		print(fromNode,end=' ')
		l.append(int(toNode))
		print(fromNode,', 1',sep='',file=v_file)
		node_under_processing = fromNode
if l!=[]:
	#print(" ".join(l))
	print(" ",l)
