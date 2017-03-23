import re
from pprint import pprint

# File content
xml = [
    "<xml>",
    "<name gender=\"men\">Ashot</name>",
    "<user>tosha</user>",
    "<another_tag>tosha</user>",
    "<tag>tosha</teg>",
    "<last_tag/>",
    "</xml>"
]

# Regex for tags.
open_tag_regex = re.compile("<(\w+/?)[>\s]")
close_tag_regex = re.compile(".*?(</(\w+)>)")
counter_dict = {}

for line in xml:
    # Find opening tag
    if open_tag_regex.match(line):
        # If matched open tag add the tag name as dictionary key and +1
        res = open_tag_regex.match(line)
        if res.group(1) in counter_dict:
            # If the tag is already in the dictionary, add 1 to the counter
            counter_dict[res.group(1)] += 1
        else:
            # Otherwise create new key
            counter_dict[res.group(1)] = 1

    # Find closing tag
    if close_tag_regex.match(line):
        # If matched close tag add the tag name as dictionary key and +1
        res = close_tag_regex.match(line)
        if res.group(2) in counter_dict:
            if counter_dict[res.group(2)] < 1:
                print "Found closing tag without matching opening {}".format(res.group(1))
            # If the tag is already in the dictionary, subtract 1 from the counter
            counter_dict[res.group(2)] -= 1
        else:
            print "Found closing tag without matching opening {}".format(res.group(1))

pprint(counter_dict)
