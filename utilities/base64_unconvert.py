# Syntax: 
# python3 base64_unconvert.py [base64 string] 

import base64
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_str')
args = parser.parse_args()
arg1 = args.input_str

decoded  = arg1.encode('ascii')
bse64_bytes = base64.b64decode(decoded)
bse64_message = bse64_bytes.decode('ascii')

print(arg1, ':', bse64_message)
