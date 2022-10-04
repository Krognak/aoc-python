import re
from pathlib import Path

data = Path("2015/day12/input.txt").read_text()

m = re.findall(r"-?\d+", data)
print(sum(map(int, m)))
