from ipaddress import ip_network, ip_address

def find_best_route(routes, destination):
    destination_ip = ip_address(destination)
    best_route = None
    max_prefix_length = -1

    for route in routes:
        network = ip_network(route)
        if destination_ip in network and network.prefixlen > max_prefix_length:
            best_route = route
            max_prefix_length = network.prefixlen

    return best_route

# ルーティングテーブルのエントリ
routes = [
    "0.0.0.0/0",      # (a)
    "192.168.0.0/21", # (b)
    "192.168.8.0/21"  # (c)
]

# 宛先IPアドレス
destination_ip = "192.168.6.123"

# 最適なルートを見つける
best_route = find_best_route(routes, destination_ip)
print(best_route)
