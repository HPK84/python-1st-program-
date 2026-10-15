import re

s = "cat bat cat"

print(re.findall("cat", s))
print(re.sub("cat", "dog", s))
print(re.split(" ", s))
print(re.search("bat", s).group())