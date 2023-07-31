# Syntax:
# python3 hash_md5.py [cleartext string]

import hashlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_str')
args = parser.parse_args()
arg1 = args.input_str

hash_input = hashlib.md5(str(arg1).encode('utf-8'))
print('Hash: ', hash_input.hexdigest())
