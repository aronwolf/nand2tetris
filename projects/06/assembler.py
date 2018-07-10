import sys

comp_table = {
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

dest_table = {
    'null': '000',
    'M': '001',
    'D': '010',
    'MD': '011',
    'A': '100',
    'AM': '101',
    'AD': '110',
    'AMD': '111',
}

jump_table = {
    'null': '000',
    'JGT': '001',
    'JEQ': '010',
    'JGE': '011',
    'JLT': '100',
    'JNE': '101',
    'JLE': '110',
    'JMP': '111',
}

def assembler(filename):
    code = []
    with open(filename, "r") as f:
        for line in f.read().splitlines():
            if line and not line.startswith('/'):
               code.append(line)

    for line in code:
        if line.startswith('@'):
            print(assemble_a(line))
        else:
            print(assemble_c(line))

def assemble_a(line):
    value = bin(int(line[1:]))[2:].zfill(16)
    return value        

def assemble_c(line):
    try:
        dest, rest = line.split('=')
    except ValueError:
        dest, rest = 'null', line
    try:
        comp, jump = rest.split(';')
    except ValueError:
        comp, jump = rest, 'null'

    try:
        comp = comp_table[comp]
        dest = dest_table[dest]
        jump = jump_table[jump]
    except KeyError:
        raise Error('Bad C-instruction: {line}'.format(line=line))

    return '111{comp}{dest}{jump}'.format(comp=comp,
                                          dest=dest.zfill(3),
                                          jump=jump.zfill(3))

if __name__ == "__main__":
    assembler(sys.argv[1])
