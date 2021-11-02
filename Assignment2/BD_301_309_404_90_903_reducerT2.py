#!/usr/bin/python3
import sys as s
def rank(x):
    k=0.15 + (0.85 * x)
    return k
old_pg = None
old_pgrank=0
for i in s.stdin:
	i = i.strip()
	try:
		des_pg,src_pg, pg_contr = i.split(",")
		src_pg = src_pg.strip()
		des_pg = des_pg.strip()
		pg_contr = float(pg_contr.strip())
	except Exception as e:
		continue
	if old_pg is None:
		old_pg = des_pg
		old_pgrank = rank(pg_contr)
	elif old_pg == des_pg:
		old_pgrank += 0.85 * pg_contr
	else:
		print('{},{:.2f}'.format(old_pg, old_pgrank),sep='')
		old_pg = des_pg
		old_pgrank = rank(pg_contr)
print('{},{:.2f}'.format(old_pg, old_pgrank),sep='')
