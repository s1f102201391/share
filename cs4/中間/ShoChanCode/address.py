import ipaddress

def calculate_network_details(ip_with_cidr):
    # CIDR表記のIPアドレスを解析
    network = ipaddress.ip_network(ip_with_cidr, strict=False)

    # ネットワークアドレスを計算
    network_address = network.network_address

    # ブロードキャストアドレスを計算
    broadcast_address = network.broadcast_address

    # サブネットマスクを計算
    subnet_mask = network.netmask

    # 利用可能なホストIP範囲を計算
    hosts = list(network.hosts())
    first_host = hosts[0] if hosts else "N/A"
    last_host = hosts[-1] if hosts else "N/A"

    return (
        "Network Address: {}\n"
        "Broadcast Address: {}\n"
        "Subnet Mask: {}\n"
        "First Host IP: {}\n"
        "Last Host IP: {}"
    ).format(
        str(network_address),
        str(broadcast_address),
        str(subnet_mask),
        str(first_host),
        str(last_host)
    )

# 例としての使用
ip_with_cidr_example = "192.168.1.0/24"
network_details = calculate_network_details(ip_with_cidr_example)
print(network_details)
