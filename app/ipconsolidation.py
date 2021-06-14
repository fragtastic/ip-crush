import ipaddress

def consolidate(file, grouped: bool = True):
    ips = []
    count_addresses = 0
    count_networks = 0
    output = []
    for line in file:
        if not isinstance(line, str):
            line = line.decode()
        line = line.strip()
        if not line:
            continue
        try:
            addr = ipaddress.IPv4Address(line)
            ips.append(addr)
            count_addresses += 1
        except ipaddress.AddressValueError:
            if grouped:
                for network in ipaddress.collapse_addresses(ips):
                    output.append(str(network))
                    count_networks += 1
                ips = []
                output.append(line)
    # Must do this one final time since there may be nothing after the last set of addresses
    for network in ipaddress.collapse_addresses(ips):
        output.append(str(network))
        count_networks += 1
    return output, count_addresses, count_networks