import sys
import re

pattern = r"\b(\w+)\1\b"

for line in sys.stdin:
    line = line.rstrip()
    result = re.findall(pattern, line)
    if (result):
        print(line)