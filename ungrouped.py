from app.ipconsolidation import consolidate

output = []
count_addresses = 0
count_networks = 0

inFileName = 'data/testdata.txt'

with open(inFileName, 'rt') as inFile:
    output, count_addresses, count_networks = consolidate(inFile, grouped=False)

with open(f'{inFileName}_ungrouped.txt', 'wt') as outFile:
    outFile.write('\n'.join(output))

print(f'networks: {count_networks}')
print(f'addresses: {count_addresses}')
print(f'networks/addresses: {count_networks / count_addresses}')
