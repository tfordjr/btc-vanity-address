# CS 4732 Project 3 creating btc vanity addresses with SHA-256

from hashlib import sha256
import time

print('This Program will generate something similar to a BTC addess')
print('Instead of using ECC we will use SHA-256 to emulate this effect')
target = input('Enter target address:')
seed = '0'
output = ''
start = time.time()

while not output.startswith(target):
    output = sha256(seed.encode('utf-8')).hexdigest()
    print('output:', output, 'with seed', seed)
    seed = str(int(seed) + 1)

end = time.time()
print('Vanity address found in', (end-start), 'seconds:', output, 'starts with', target)