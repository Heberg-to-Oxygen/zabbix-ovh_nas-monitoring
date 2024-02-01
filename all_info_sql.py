"""
Author : Florian DJERBI
Object : Information list NAS
Creation Date : 04/28/2023
Modification Date : 04/28/2023
"""

import sys
from login import login, sql_connexion


def all_info():
    list_nas = login.get('/dedicated/nasha')
    for nas in list_nas:
        all_nas_info(nas)
        all_partition_info(nas)


def all_nas_info(nas):
    try:
        info_nas = login.get(f'/dedicated/nasha/{nas}')
        info_nas_size = login.get(f'/dedicated/nasha/{nas}/use', type='size')["value"]
        info_nas_used = login.get(f'/dedicated/nasha/{nas}/use', type='used')["value"]
        nas_capacity = round(info_nas_used * 100 / info_nas_size)
        nas_name = info_nas["serviceName"]
        nas_size = info_nas["zpoolSize"]
        nas_datacenter = info_nas["datacenter"]
        nas_ip = info_nas["ip"]
        # nas_capacity = list_partition["zpoolCapacity"]
        nas = [nas_name, nas_size, nas_capacity, nas_datacenter, nas_ip]
        request = "INSERT `ovh-nas_info` (name, size, capacity, datacenter, ip)" \
                  "VALUES (%s, %s, %s, %s, %s)" \
                  "ON DUPLICATE KEY UPDATE name=%s, size=%s, capacity=%s, datacenter=%s, ip=%s"
        val = (nas[0], nas[1], nas[2], nas[3], nas[4], nas[0], nas[1], nas[2], nas[3], nas[4])
        my_cursor = sql_connexion.cursor()
        my_cursor.execute(request, val)
        sql_connexion.commit()
    except ValueError:
        print(ValueError)
        pass


def all_partition_info(nas_name):
    list_partition = login.get(f'/dedicated/nasha/{nas_name}/partition')
    for partition in list_partition:
        try:
            info_partition = login.get(f'/dedicated/nasha/{nas_name}/partition/{partition}')
            partition_name = info_partition["partitionName"]
            partition_size = info_partition["size"]
            partition_capacity = info_partition["partitionCapacity"]
            nas = [nas_name, partition_name, partition_size, partition_capacity]
            request = "INSERT `ovh-partition_info` (nas, name, size, capacity)" \
                      "VALUES (%s, %s, %s, %s)" \
                      "ON DUPLICATE KEY UPDATE name=%s, size=%s, capacity=%s"
            val = (nas[0], nas[1], nas[2], nas[3], nas[1], nas[2], nas[3])
            my_cursor = sql_connexion.cursor()
            my_cursor.execute(request, val)
            sql_connexion.commit()
        except ValueError:
            pass


if __name__ == '__main__':
    # Test
    login = login("1133d3d6ee489f53", "761f72e4204a2e90c3a91c5ef224d4a0", "03029152ae88916e617463aa04130e9c")
    sql_connexion = sql_connexion(host="infra.vigicorp.lan", user="adm_fdjerbi", password="NbCqE97RZpvAtJwVzxrQh6ev6lP5", database="ovh-domain")
    # Prod
    # login = login(sys.argv[1], sys.argv[2], sys.argv[3])
    # sql_connexion = sql_connexion(host=sys.argv[4], user=sys.argv[5], password=sys.argv[6], database=sys.argv[7])
    all_info()
