""" Advent of Code solver class """
import sys

inp = [
    "D2FE28",
    "38006F45291200",
    "EE00D40C823060",
    "8A004A801A8002F478",
    "620080001611562C8802118E34",
    "C0015000016115A2E0802F182340",
    "A0016C880162017C3686B18A3D4780"
]
with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp += [file_handle.read().strip()]

hexd = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

"""
def decode_old(msg, total, sub=''):
    if sub == 0:
        return
    if sub != '':
        sub -= 1
    print(sub, msg)
    version = int(msg[0:3], 2)
    #total += int(msg[0:3], 2)
    print(version)
    typeid = int(msg[3:6], 2)
    rest = msg[6:]
    #print("Version:", version, "type:", typeid, "msg:", rest)
    # typeid == 4 literal value
    if typeid == 4:
        literal = ''
        last = False
        while last == False:
            literal += rest[1:5]
            if rest[:1] == '0':
                last = True
            rest = rest[5:]
            print("literal:", int(literal, 2))
        if rest != '' and int(rest, 2) != 0:
            total += decode_old(rest, total, sub)
    # otherwise: operator package
    else:
        operator = rest[:1]
        rest = rest[1:]
        # 0 operator package 15 bits
        if operator == '0':
            length = int(rest[0:15], 2)
            print("op with length", length)
            total += decode_old(rest[15:15+length], total)
        # 1 operator package 11 bits
        elif operator == '1':
            number = int(rest[0:11], 2)
            print("op with", number, "subpackets")
            total += decode_old(rest[11:], total, number)
    return total

binary_input_string = "01010101"

def decode_package(msg, i, end=sys.maxsize, sub=''):
    if sub == 0:
        return 0
    if sub != '':
        sub -= 1
    if i > len(msg):
        return 0
    version = int(msg[i:i+3], 2)
    typeid = int(msg[i+3:i+6], 2)
    i += 6
    if typeid == 4:
        literal = ''
        while int(msg[i:], 2) != 0 and i < len(msg) and i < end:
            literal += msg[i+1:i+5]
            if msg[i:i+1] == '0':
                break
            i += 5
        if msg[i+5:] != '' and int(msg[i+5:], 2) != 0:
            version += decode(msg, i+5, end=end, sub=sub)
    else:
        operator = msg[i:i+1]
        if operator == '0':
            length = int(msg[i+1:i+16], 2)
            version += decode(msg, i+16, end=i+16+length)
        elif operator == '1':
            number = int(msg[i+1:i+12], 2)
            version += decode(msg, i+12, sub=number)
    return version

print(decode_package(binary_input_string, 0))

"""

def decode(msg, i, end=sys.maxsize, sub=''):
    """ Takes binary, decodes into packages """
    #print("i", i, "end", end)
    #print(sub, msg[i:])
    if sub == 0:
        return 0
    if sub != '':
        sub -= 1
    if i > len(msg):
        return 0
    version = int(msg[i:i+3], 2)
    print("version:", version)
    typeid = int(msg[i+3:i+6], 2)
    print("type:", typeid)
    i += 6
    #print("Version:", version, "type:", typeid, "msg:", rest)
    # typeid == 4 literal value
    if typeid == 4:
        literal = ''
        while int(msg[i:], 2) != 0 and i < len(msg) and i < end:
            #print(int(msg[i+5:], 2), "i", i+5, "end", end, "len msg", len(msg))
            print("literal added:", msg[i:i+5])
            #print("rest", msg[i+6:])
            #print("ttighjisdg", msg[i:i+1])
            #print("total", msg[i:], "added", msg[i+1:i+5])
            literal += msg[i+1:i+5]
            if msg[i:i+1] == '0':
                break
            i += 5
        print("literal:", int(literal, 2), literal)
        if msg[i+5:] != '' and int(msg[i+5:], 2) != 0:
            print("continue with", msg[i+5:], "end", end, "sub", sub)
            version += decode(msg, i+5, end=end, sub=sub)
    # otherwise: operator package
    else:
        operator = msg[i:i+1]
        # 0 operator package 15 bits
        if operator == '0':
            length = int(msg[i+1:i+16], 2)
            print("op with length", length)
            version += decode(msg, i+16, end=i+16+length)
        # 1 operator package 11 bits
        elif operator == '1':
            number = int(msg[i+1:i+12], 2)
            print("op with", number, "subpackets")
            version += decode(msg, i+12, sub=number)
    return version

def task1():
    """ Task 1 solver """
    # convert hex input to binary
    inp_bin = []
    for package in inp:
        bin = ''
        for char in package:
            bin += hexd[char]
        inp_bin.append(bin)
    
    #print(inp[0], decode(inp_bin[0], 0))
    #print(inp[1], decode(inp_bin[1], 0))
    #print(inp[2], decode(inp_bin[2], 0))
    #print(inp[3], decode(inp_bin[3], 0))
    #print(inp[4], decode(inp_bin[4], 0))
    #print(inp[5], decode(inp_bin[5], 0))
    #print(inp[6], decode(inp_bin[6], 0))
    #print(inp[7])
    return decode(inp_bin[7], 0)

print("Task 1:", task1())

def task2():
    """ Task 2 solver """
    result = 0
    return result

#print("Task 2:", task2())
