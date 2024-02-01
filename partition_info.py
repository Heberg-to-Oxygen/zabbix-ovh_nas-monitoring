"""
Author : Florian DJERBI
Object : Information on partition for NAS OVH
Creation Date : 03/08/2023
Modification Date : 03/16/2023
"""

import json
import sys
from login import login


def partition_info(nas, partition):
    info_partition = login.get(f'/dedicated/nasha/{nas}/partition/{partition}')
    partition_name = info_partition["partitionName"]
    partition_size = info_partition["size"]
    partition_capacity = info_partition["partitionCapacity"]
    list_all = {"NAS": nas, "Partition": partition_name, "Size": partition_size, "Capacity": partition_capacity}
    return list_all


if __name__ == '__main__':
    # Test
    login = login("1133d3d6ee489f53", "761f72e4204a2e90c3a91c5ef224d4a0", "03029152ae88916e617463aa04130e9c")
    print(json.dumps(partition_info("zpool-001829", "customers")))
    # Prod
    # login = login(sys.argv[1], sys.argv[2], sys.argv[3])
    # print(json.dumps(partition_info(sys.argv[4], sys.argv[5])))
