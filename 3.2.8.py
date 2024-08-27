import sys
import re

pattern = r"\b(\w)(\w)"
repl = r"\2\1"

for line in sys.stdin:
    line = line.rstrip()
    result = re.sub(pattern, repl, line)
    print(result)