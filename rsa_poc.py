# RSA Proof of Concept
# NOT CRYPTOGRAPHICALLY SECURE
import sys
import argparse
import math

# read public key file
# n, e seperated by newline
# returns (n, e) as a tuple
def read_pub_key(pub_key):
    try:
        return tuple(open(pub_key).read().splitlines())
    except:
        sys.exit("failed to read public key")

def decrypt(ciphertext, priv_key, pub_key):
    pub_key_tuple = read_pub_key(pub_key)
    try:
        d = int(open(priv_key).read())
    except:
        print("error reading private key")

    plaintext = ""
    # split ciphertext into space-delineated 'words' representing plaintext chars
    for word in ciphertext.split():
        plaintext += str(word^d % pub_key_tuple[0])
    return plaintext

# very basic ecb mode implementation, encrypts each char sequentially
def encrypt(plaintext, pub_key):
    #pub_key_tuple = read_pub_key(pub_key)
    ciphertext = ""
    for line in plaintext:
        for char in line:
            # cipher = plain_char^(e) mod (n)
            ciphertext += str(ord(char)^int(pub_key[0]) % int(pub_key[1]))
            # add space between encrypted chars
            ciphertext += ' '
    return ciphertext

# PLACEHOLDER
def keygen():

    # generate two primes similar size
    p1 = 61
    p2 = 53

    # multiply the two to get n
    n = p1*p2

    # pick small odd e
    # ensure coprime with phi=(p1-1)(p2-1)
    # 65537 is the standard
    e = 17

    # calculate private exponent d = (2*phi(n)+1)/e
    #return (2*((p1-1)*(p2-1))+1)/e

    d = pow(e, -1, math.lcm((p1-1),(p2-1)))

    print(f"Private key: {n}, {d}")
    print(f"Public key: {n}, {e}")

## HELPER FUNCTIONS



# random prime generator
# miller-rabin method simpler
# consider gordon's algo for strong prime generation
# k = target no. bits (i.e. 2^k)
# t = security parameter
#def gen_prime(int k, int t):


# selecting e
# 65537 is the standard


# calculating private exponent d given phi(n) and d

if __name__ == "__main__":
    print("This is a toy implementation of RSA and not secure!")
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_text', type=str, help="Input string to be encrypted/decrypted")
    parser.add_argument('-pub', '--pub_key', type=argparse.FileType('r'), help="Public key file")
    parser.add_argument('-priv', '--priv_key', type=argparse.FileType('r'), help="Private key file")
    parser.add_argument('-e', action="store_true", default=False)
    parser.add_argument('-d', action="store_true", default=False)
    parser.add_argument('-k', action="store_true", default=False)
    args = parser.parse_args()


    if args.k:
        keygen()
    elif args.e:
        with args.pub_key as p_key:
            pub_key = tuple(p_key.read().splitlines())
            print(encrypt(args.input_text, pub_key))
    elif (args.d):
        print(decrypt(args.input_text, priv_key, pub_key))