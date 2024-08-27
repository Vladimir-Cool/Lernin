import sys
import re

pattern = "human"
repl = "computer"

for line in sys.stdin:
    line = line.rstrip()
    result = re.sub(pattern, repl, line)
    print(result)
