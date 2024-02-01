"""
Author : Florian DJERBI
Object : Information list NAS
Creation Date : 03/08/2023
Modification Date : 04/28/2023
"""

import json
import sys
from login import login, sql_connexion


def nas_list():
    list_nas = login.get('/dedicated/nasha')
    return list_nas


def nas_info(nas):
    info_nas = login.get(f'/dedicated/nasha/{nas}')
    info_nas_size = login.get(f'/dedicated/nasha/{nas}/use', type='size')["value"]
    info_nas_used = login.get(f'/dedicated/nasha/{nas}/use', type='used')["value"]
    nas_capacity = round(info_nas_used * 100 / info_nas_size)
    nas_name = info_nas["serviceName"]
    nas_size = info_nas["zpoolSize"]
    # nas_capacity = list_partition["zpoolCapacity"]
    list_all = {"NAS": nas_name, "Size": nas_size, "Capacity": nas_capacity}
    return list_all


def all_nas_info():
    list_nas = login.get('/dedicated/nasha')
    for i in list_nas:
        list_partition = login.get(f'/dedicated/nasha/{i}')
        print(list_partition)
        nas_name = list_partition["serviceName"]
        nas_size = list_partition["zpoolSize"]
        nas_capacity = list_partition["zpoolCapacity"]
        print({"NAS": nas_name, "Size": nas_size, "Capacity": nas_capacity})


if __name__ == '__main__':
    # Test
    login = login("1133d3d6ee489f53", "761f72e4204a2e90c3a91c5ef224d4a0", "03029152ae88916e617463aa04130e9c")
    sql_connexion = sql_connexion(host="infra.vigicorp.lan", user="adm_fdjerbi", password="NbCqE97RZpvAtJwVzxrQh6ev6lP5", database="ovh-domain")
    print(json.dumps(nas_info("zpool-128463")))
    # Prod
    # login = login(sys.argv[1], sys.argv[2], sys.argv[3])
    # print(json.dumps(nas_partition_info(sys.argv[4])))

