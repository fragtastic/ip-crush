import ipaddress


ips = []
count_addresses = 0
count_networks = 0

inFileName = 'CHANGEME.txt'

with open(inFileName, 'rt') as inFile, open(f'grouped_{inFileName}', 'wt') as outFile:
    for line in inFile:
        try:
            addr = ipaddress.IPv4Address(line.strip())
            ips.append(addr)
            count_addresses += 1
        except ipaddress.AddressValueError:
            for network in ipaddress.collapse_addresses(ips):
                outFile.write(f'{network}\n')
                count_networks += 1
            ips = []
            outFile.write(line)

print(f'networks: {count_networks}')
print(f'addresses: {count_addresses}')
print(f'networks/addresses: {count_networks / count_addresses}')
