import re
import sys
search_string = 'hello world'
pattern = 'hello world'

match = re.match(pattern,search_string)

if match:
    print("regex matches")

print(len(sys.argv))
pattern = sys.argv[0]
search_string = sys.argv[0]

match = re.match(pattern, search_string)
if match:
    template = "'{}' matches pattern '{}'"
else:
    template = "'{}' does not match pattern '{}'"
print(template.format(search_string, pattern))