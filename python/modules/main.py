import mod
from color50 import rgb, constants
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=int, required=True)
args = parser.parse_args()
print(args.name)

# my_color = rgb(128, 0, 128)
# print(my_color + "Hello, World!" + constants.RESET)

# mod.foo()
