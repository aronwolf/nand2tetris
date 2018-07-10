import sys
import regex as re

comp_values = {
    '0': '0101010',
    '1': '0111111',
    '-1': '0111010',
    'D': '0001100',
    'A': '0110000',
    '!D': '0001101',
    '!A': '0110001',
    '-D': '0001111',
    '-A': '0110011',
    'D+1': '0011111',
    'A+1': '0110111',
    'D-1': '0001110',
    'A-1': '0110010',
    'D+A': '0000010',
    'D-A': '0010011',
    'A-D': '0000111',
    'D&A': '0000000',
    'D|A': '0010101',
    'M': '1110000',
    '!M': '1110001',
    '-M': '1110011',
    'M+1': '1110111',
    'M-1': '1110010',
    'D+M': '1000010',
    'D-M': '1010011',
    'M-D': '1000111',
    'D&M': '1000000',
    'D|M': '1010101',
}

dest_values = {
    'M': '001',
    'D': '010',
    'MD': '011',
    'A': '100',
    'AM': '101',
    'AD': '110',
    'AMD': '111',
}

jump_values = {
    'JGT': '001',
    'JEQ': '010',
    'JGE': '011',
    'JLT': '100',
    'JNE': '101',
    'JLE': '110',
    'JMP': '111',
}

def assembler(filename):
    clean_code = []
    with open(filename, "r") as f:
        for line in f.read().splitlines():
            if line and not line.startswith('/'):
               clean_code.append(line)

    for line in clean_code:
        if line.startswith('@'):
            print(parse_a(line))
        else:
            print(parse_c(line))

def parse_a(line):
    value = bin(int(line[1:]))[2:].zfill(16)
    return value        

def parse_c(line):
    value1 = re.split('=|;', line)
    value2 = re.findall("^.*\d?=(.*\d?)$", line)
    value3 = re.findall("^.*\d?;(.*\d?)$", line)
    if '=' in line:
        return '111{value2}{value1}000'.format(value2=comp_values[value2[0]], value1=dest_values[value1[0]])
    else:
        return '111{value1}000{value3}'.format(value1=comp_values[value1[0]], value3=jump_values[value3[0]])
    

if __name__ == "__main__":
    assembler(sys.argv[1])
