import ipaddress # biblioteca para criar/poke/manipular endereços e redes IPv4 e IPv6.

ip = '192.168.0.0/24'

rede = ipaddress.ip_network(ip, strict=False)

for ip in rede:
    print(ip)
