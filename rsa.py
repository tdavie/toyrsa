# RSA Proof of Concept
# NOT CRYPTOGRAPHICALLY SECURE
import sys
import argparse
import math
import secrets
import random

# read key file
# return values separated by newline as a tuple of ints
def read_key(key_file):
    with key_file as f:
        return tuple(map(int, f))

def decrypt(ciphertext, priv_key):
    plaintext = ""
    #print(f"{priv_key[0]}, {priv_key[1]}")
    # split ciphertext into space-delineated blocks
    for block in ciphertext.split():
        #print(block)
        #decrypt_block = (str(int(block)**priv_key[1] % priv_key[0])).zfill(3)
        decrypt_block = str(chinese_remainder_decrypt(int(block), priv_key)).zfill(3)
        #print(int(block)**priv_key[1] % priv_key[0])
        #print(decrypt_block)
        for i in range(int(len(decrypt_block)/3)):
            plaintext += chr(int(decrypt_block[i*3:(i+1)*3]))
            #print(int(decrypt_block[i*3:(i+1)*3]))
    return plaintext

def chinese_remainder_decrypt(ciphertext, priv_key):
    assert len(priv_key) == 4
    dp = priv_key[1] % (priv_key[2] - 1)
    dq = priv_key[1] % (priv_key[3] - 1)
    qinv = pow(priv_key[3], -1, priv_key[2])
    m1 = pow(ciphertext, dp, priv_key[2])
    m2 = pow(ciphertext, dq, priv_key[3])
    h = qinv * (m1 - m2) % priv_key[2]
    return m2 + (h * priv_key[3] % (priv_key[2] * priv_key[3]))
""" Returns ciphertext encrypted using electronic codebook mode

"""
def encrypt(plaintext, pub_key, block_size):
    # append spaces until block size evenly divides message length
    while True:
        if (len(plaintext) % block_size == 0):
            break
        plaintext += ' '

    ciphertext = ""
    block = ""
    for x, char in enumerate(plaintext):
        # append ascii char code digits to block string
        # mod 127 to ensure only ascii, pad 0s to 3 digits
        block += str((ord(char) % 127)).zfill(3)
        # encrypt block once 'full'
        if ((x + 1) % block_size == 0):
            #print(block)
            ciphertext += str((int(block)**pub_key[1]) % pub_key[0])
            # add space between blocks
            #print(ciphertext)
            ciphertext += ' '
            block = ""
    return ciphertext

""" Returns ciphertext encrypted using cipher block chaining mode


def cbc_encrypt(plaintext, pub_key, block_size):
        
    # append spaces until block size evenly divides message length
    while True:
        if (len(plaintext) % block_size == 0):
            break
        plaintext += ' '

    #b_plaintext = bytearray(plaintext, 'utf-8')
    iv = secrets.randbits(block_size * 8)
    # initialisation vector prepended to ciphertext
    # doesn't need to be secret, but is necessary for decrypting
    ciphertext = str(iv) + '\n'

    for i in range((len(plaintext)/block_size)-1):
        block = plaintext[i * block_size : (i+1) * block_size]
        cipherblock = xor_block(block, iv)
        
            # block cipher encryption
        cipherblock = block_bytes ** priv_key[1] % priv_key[0]
        ciphertext += cipherblock.decode(encoding="ascii")
        iv = cipherblock

# XOR block with initialisation value / prev encrypted block
def xor_block(block, iv):
    return bytes(ord(c)^k for c, k in zip(block, iv))
"""


""" Returns randomly generated public and private keys

n specifies approximate number of bits of each prime
"""
def keygen(n):
    # generate two primes similar size
    # ensure they can't be equal
    # t = 40 per justification below
    while True:
        p1 = gen_prime(n, 40)
        p2 = gen_prime(n, 40)
        if p1 != p2:
            break

    n = p1*p2

    # pick small odd e, 65537 is the standard
    # no security implications for keeping it fixed
    e = 65537   

	# calculate private exponent
	# d = modular multiplicative inverse of e modulo lambda(n)
    d = pow(e, -1, math.lcm((p1-1),(p2-1)))

    print(f"Private key: {n}, {d}, {p1}, {p2}")
    print(f"Public key: {n}, {e}")

# random prime generator
# miller-rabin method simpler
# consider gordon's algo for strong prime generation
# k = target no. bits (i.e. 2^k)
# t = security parameter
def gen_prime(k, t):
	while True:
		# generate random odd of ~k bits
		n = 2*secrets.randbits(int(k/2))+1
		if miller_rabin(n, t):
			return n

""" Return boolean primality of n

Miller-rabin primality test
This implementation modified from https://gist.github.com/Ayrx/5884790
"""
def miller_rabin(n, k):

    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

if __name__ == "__main__":
    print("This is a toy implementation of RSA and not secure!")
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_text', type=str, help="Input string to be encrypted/decrypted")
    parser.add_argument('-pub', '--pub_key', type=argparse.FileType('r'), help="Public key file")
    parser.add_argument('-priv', '--priv_key', type=argparse.FileType('r'), help="Private key file")
    parser.add_argument('-b', '--block_size', type=int, help="block size for encryption")
    parser.add_argument('-e', action="store_true", default=False)
    parser.add_argument('-d', action="store_true", default=False)
    parser.add_argument('-k', type=int, default=False)
    args = parser.parse_args()

    if args.k:
        keygen(args.k)
    elif args.e:
        with args.pub_key as pub_key:
            print(encrypt(args.input_text, read_key(pub_key), args.block_size))
    elif args.d:
        with args.priv_key as priv_key:
            print(decrypt(args.input_text, read_key(priv_key)))