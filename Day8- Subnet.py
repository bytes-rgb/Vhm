import ipaddress

main_network = ipaddress.IPv4Network("192.168.1.0/24")

subnets = list(main_network.subnets(prefixlen_diff=2))

for subnet in subnets:
    print(subnet)