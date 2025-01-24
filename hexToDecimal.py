from argparse import ArgumentParser 

parser = ArgumentParser()
parser.add_argument('--input', type=str)
args = parser.parse_args()


hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    if len(hexNum) > 3:
        return None
    result = 0
    reversedHexa = hexNum[::-1]
    multipliers = [1, 16, 256]
    index = 0
    for hex in reversedHexa:
        if hex not in hexNumbers:
            return None
        result = result + (int(hexNumbers[hex]) * multipliers[index])
        index = index + 1        
    return result
    
result = hexToDec(args.input)
print(f'Converted hex {args.input} to {result}')