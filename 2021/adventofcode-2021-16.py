from functools import reduce
from operator import add, mul, gt, lt, eq

with open('input16', 'r') as f:
    d = {(str(i) if i <= 9 else chr(ord('A') + i % 10)): bin(i)[2:].zfill(4) for i in range(16)}
    # Convert to binary string
    bin_str = ''.join([d[j] for j in f.read().strip()])


# to get the literal value when type_id is 4, also return the remaining string
def literal_value(bin_string):
    value = ""
    while True:
        value += bin_string[1:5]
        if bin_string[0] == '0':
            break
        bin_string = bin_string[5:]
    return int(value, 2), bin_string[5:]


# find sub packets if the packet is not a literal, find version sum along the way, no need to calculate again
def find_sub_packets(bin_string, packet, identifier):
    if identifier == "0":
        len_of_whole_packet = int(bin_string[:15], 2)
        to_check = bin_string[15:15 + len_of_whole_packet]
        rem = bin_string[15 + len_of_whole_packet:]
        while to_check:
            sub_packet, to_check = get_packet(to_check)
            packet["children"].append(sub_packet)
            packet['version_sum'] += sub_packet['version_sum']
    else:
        total_sub_packets = int(bin_string[:11], 2)
        rem = bin_string[11:]
        for _ in range(total_sub_packets):
            sub_packet, rem = get_packet(rem)
            packet["children"].append(sub_packet)
            packet['version_sum'] += sub_packet['version_sum']
    return packet, rem


# recursively get the packet with sub packets
def get_packet(bin_string):
    packet = {
        'version': int(bin_string[:3], 2),
        'type_id': int(bin_string[3:6], 2),
        'children': list(),
        'version_sum': int(bin_string[:3], 2)
    }
    if packet['type_id'] == 4:
        packet['value'], rem = literal_value(bin_string[6:])
        return packet, rem
    return find_sub_packets(bin_string[7:], packet, bin_string[6])


# Final solve to get the evaluation of the packet, pass the reduce to int, for boolean evalution
def solve(packet):
    if packet['type_id'] == 4:
        return packet['value']
    return int(reduce([add, mul, min, max, lambda x: 'Glad,You are looking here ;-). Comment and let me know, whos there?', gt, lt, eq][packet['type_id']],
                      [solve(i) for i in packet['children']]))


final_packet, waste = get_packet(bin_str)
print(f'Version sum: {final_packet["version_sum"]}')
print(f'Final Solve : {solve(final_packet)}')
