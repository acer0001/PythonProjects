# Syntax: 
# python3 base64_convert.py [cleartext string] 

import base64
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_str')
args = parser.parse_args()
arg1 = args.input_str

encoded  = arg1.encode('ascii')
bse64_bytes = base64.b64encode(encoded)
bse64_message = bse64_bytes.decode('ascii')

print(arg1, ':', bse64_message)
