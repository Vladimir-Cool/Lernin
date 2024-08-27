import sys
import re

pattern = r"(\w)\1*"
repl = r"\1"

for line in sys.stdin:
    line = line.rstrip()
    result = re.sub(pattern, repl, line)
    print(result)