#!/usr/bin/python
import os
import sys

if (len(sys.argv) <= 1):
    print("Usage: crtsh.py <DOMAIN>")
    sys.exit(1)

domain = str(sys.argv[1])
print("Domain being searched : " + domain)

query = "curl -s https://crt.sh/\\?q\\=\\%." + domain  + "\\&output\\=json | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u"
print("Bash command : " + query)
print("---------------------------")
os.system(query)