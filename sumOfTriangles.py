from argparse import ArgumentParser 

parser = ArgumentParser()
parser.add_argument('--number', type=int)
args = parser.parse_args()

def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)

def square(num):
    if type(num) == int:
        if num < 0 or num > 998:
            return " Please enter from 0 til 998, due to recursive approach"
        result = triangle(num) + triangle(num - 1)
        return result
    return None

result = square(args.number)
print(f'Result for {args.number} is {result if result else "No result"}')