#!/usr/bin/python
import subprocess
import sys
import time


#change accordingly, this was really tempermental
timeDelayBetweenReqs = 0.05

if (len(sys.argv) <= 1):
    print("Usage: crtsh.py <domain file>")
    sys.exit(1)



domainFile = str(sys.argv[1])

with open(domainFile, "r") as f:
    domains = f.readlines()
    for i in domains:
        p1 = subprocess.Popen(["python", "/opt/crt.sh/crtshSilent.py", i.strip() ])
        p1.wait()