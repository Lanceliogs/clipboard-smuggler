import base64
import os
import argparse
import codecs

parser = argparse.ArgumentParser(prog='Clipboard Smuggler',
                                 description='Use case: Need to send files through VNC that only supports clipboard.',
                                 epilog='Delivered by the greatest smuggler of the galaxy: Lan Solo!')

parser.add_argument('--file', '-f', help='The path of the goods to smuggle', required=True)
parser.add_argument('--output', '-o', help='Where to drop the payload script', default='payload.py')

args = parser.parse_args()

print ('''
##### Clipboard Smuggler #####
       
Greatest smuggler in the galaxy Lan Solo reporting!
I'll prep a nice package for you...
Let me look at the goods...
''')

filename = os.path.basename(args.file)

goods = ''
count = 0
size = 0
with open(args.file, 'rb') as f:
    while True:
        chunk = f.read(1024)
        if len(chunk) == 0:
            break
        goods = goods + codecs.decode(base64.b64encode(chunk), encoding='utf-8')
        count = count + 1
        size = size + len(chunk)
        if count % 100 == 0:
            print(f'{size / 1024} bytes read\r')

print (f'Reading completed: {size} bytes')
print (f'Payload size: {len(goods)} chars')

with open(args.output, 'w', encoding='utf-8') as f:
    f.write(f'import base64\nimport os\n\n')
    f.write("print('##### Clipboard Smuggler Payload Script #####')\n")
    f.write(f"print('*SWOOOOOSH!!!* Lan Solo here! I have some goods to deliver!')\n")
    f.write(f"print('Payload size: {len(goods)} chars')\n")
    f.write(f"barr = base64.b64decode('{goods}')\n")
    f.write(f"with open('{filename}', 'wb') as f:\n")
    f.write("    f.write(barr)\n")
    f.write("print('Job complete. See ya!')\n")

print(f'Payload file: {args.output} created successfully.')