"""
Author : Florian DJERBI
Object : List NAS OVH
Creation Date : 03/08/2023
Modification Date : 03/16/2023
"""

import json
import sys
from login import login


def nas_list():
    list_all = []
    list_nas = login.get('/dedicated/nasha')
    for i in list_nas:
        list_all.append({"NAS": i})
    return list_all


if __name__ == '__main__':
    login = login("1133d3d6ee489f53", "761f72e4204a2e90c3a91c5ef224d4a0", "03029152ae88916e617463aa04130e9c")
    # login = login(sys.argv[1], sys.argv[2], sys.argv[3])
    print(json.dumps(nas_list()))
