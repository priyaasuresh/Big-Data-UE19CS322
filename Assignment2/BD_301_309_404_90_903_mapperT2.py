#!/usr/bin/python3
import sys
import json
import math
def similar(a,b):
	k=0
	asqr=0;bsqr=0;
	if len(a)==len(b):
		for i in range(len(a)):
			k=k+(a[i]*b[i])
			asqr=asqr+(a[i]*a[i])
			bsqr=bsqr+(b[i]*b[i])

		return k/((math.sqrt(asqr))*math.sqrt(bsqr))

	else:
		return 1
f = open(sys.argv[2].strip(),)
data = json.load(f)
pg_rank = dict()
with open(sys.argv[1].strip()) as vfile:
	lines = vfile.read().strip().split("\n")
	for i in lines:
		try:
			page, rank = i.split(",")
		except Exception as e:
			continue
		pg_rank[page.strip()] = float(rank.strip())
for i in sys.stdin:
	i = i.strip()
	try:
		srcNode, destNodes = i.split("\t")
		srcNode = srcNode.strip()
		destNodes = eval(destNodes.strip())
	except Exception as e:
		continue

	num_outgoing_links = len(destNodes)
	srcNode_pg_rank = pg_rank[srcNode]
	try:
		srcNode_contribution = srcNode_pg_rank * (1 / num_outgoing_links)
	except Exception as e:
		continue
	print(f"{srcNode}\t,0\t,0")
	for node in destNodes:

		#if node in pg_rank.keys():
		final_contr=0
		similarity=similar(data[str(int(srcNode))],data[str(int(node))])
		final_contr=srcNode_contribution*similarity
		print("{}\t,{}\t,{}".format(node,srcNode,final_contr))
