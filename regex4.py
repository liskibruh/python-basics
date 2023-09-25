import re

content = "watch?v=nX5ONgCdLcc"

pattern = re.compile(r"watch\?v=[A-Za-z0-9_-]{11}")
matches = pattern.finditer(content)
for match in matches:
	print(match)