import ipaddress


ips = []
count_addresses = 0
count_networks = 0

inFileName = 'CHANGEME.txt'

with open(inFileName, 'rt') as inFile:
    for line in inFile:
        line = line.strip()
        try:
            addr = ipaddress.IPv4Address(line)
            ips.append(addr)
            count_addresses += 1
        except ipaddress.AddressValueError:
            pass

cidr = ipaddress.collapse_addresses(ips)

with open(f'ungrouped_{inFileName}', 'wt') as outFile:
    for network in cidr:
        count_networks += 1
        outFile.write(f'{network}\n')

print(f'networks: {count_networks}')
print(f'addresses: {count_addresses}')
print(f'networks/addresses: {count_networks / count_addresses}')
