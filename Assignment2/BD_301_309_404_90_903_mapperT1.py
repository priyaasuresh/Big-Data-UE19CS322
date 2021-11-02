#!/usr/bin/python3
import sys as s
for line in s.stdin:
  try:
      line = line.strip()
      start = line[0] == "#"
      if start:
          continue
      else:
            ele = line.split()
            from_node,to_node = ele
            from_node = from_node.strip()
            to_node = to_node.strip()
            print(from_node,"\t",to_node)
  except Exception:
      continue
