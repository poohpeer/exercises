import re
# File content
xml = [
    "<xml>",
    "<name gender=\"men\">Ashot</name>",
    "<user>tosha</user>",
    "</last_tag>",
    "</xml>"
]

tag_regex = re.compile("<(/?\w+)[>\s].*?")
counter_dict = {}

for line in xml:
    res = tag_regex.match(line)
    if res:
        counter_dict[res.group(1)] = 1
