import sys
import re

pattern = r"\b[aA]+\b"
repl = "argh"

for line in sys.stdin:
    line = line.rstrip()
    result = re.sub(pattern, repl, line, 1)
    print(result)