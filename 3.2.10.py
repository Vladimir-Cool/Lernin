import sys
import re

pattern = r"^11|101+01|1001|00|$"
# pattern = r"^(1(01*)*1|0)+$"

for line in sys.stdin:
    line = line.rstrip()
    result = re.match(pattern, line)
    print(result)