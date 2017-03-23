import os
from pprint import pprint

my_dict = {
    "name": "Schultz",
    "color": "Niger",
    "using_drugs": [
        "optalgin",
        "advil",
        "acamol"
    ],
    "cats": {
        1 : "putty",
        2 : "lizi"
    }
}

print my_dict

print "-" * 40
pprint(my_dict, width=1)
