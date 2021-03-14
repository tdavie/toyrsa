# RSA Proof of Concept
# NOT CRYPTOGRAPHICALLY SECURE
import sys
import argparse

if __name__ == "__main__":
    print("This is a toy implementation of RSA and not secure!")
    parser = argparse.ArgumentParser()
    parser.parse_args
    # todo add args for encrypt, decrypt, keygen


def decrypt(ciphertext, priv_key, pub_key):
    try:
        pub_key_tuple = read_pub_key(pub_key)
    except:
        print("error reading public key")
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
    try:
        pub_key_tuple = read_pub_key(pub_key)
    except:
        print("error reading public key")
    ciphertext = ""
    for char in plaintext:
        # cipher = plain_char^(e) mod (n)
        ciphertext += str(char^pub_key_tuple[0] % pub_key_tuple[1])
        # add space between encrypted chars
        ciphertext += ' '
    return ciphertext

# PLACEHOLDER
def keygen():

    # generate two primes similar size
    p1 = 241
    p2 = 251

    # multiply the two to get n
    n = p1*p2

    # pick small odd e
    # ensure coprime with phi=(p1-1)(p2-1)
    # 65537 is the standard
    e = 3

    # calculate private exponent d = (2*phi(n)+1)/e
    return (2*((p1-1)*(p2-1))+1)/e
}

## HELPER FUNCTIONS

# read public key file
# n, e seperated by newline
# returns (n, e) as a tuple
def read_pub_key(pub_key):
    return tuple(open(pub_key).read().splitlines())


# random prime generator
# miller-rabin method simpler
# consider gordon's algo for strong prime generation
# k = target no. bits (i.e. 2^k)
# t = security parameter
#def gen_prime(int k, int t):


# selecting e
# 65537 is the standard


# calculating private exponent d given phi(n) and d