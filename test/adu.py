import re

str_match = re.match('^a(\d+)','a33333b')
print(str_match.group(1))
