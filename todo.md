Stage 1: Encrypt and decrypt using preset keypair
[x] Pseudocode, general program structure
[x] Write encryption algorithm taking a given keypair
[x] Write decryption algorithm taking a given keypair
[x] Write key generation algorithm, with correct process but substituting pre-generated primes + e
[ ] Implement CLI using argparse
[ ] Test and bug-fix

Stage 2: Add ability to generate + export keypairs
[ ] Create miller-rabin method prime generator
[ ] Add checks for p1, p2 coprime with e
[ ] Add helpers and cli arguments for import/export to file
[ ] Test and bug-fix

Stage 3: Cryptographic hardening
[ ] Strong prime generation -- gordon's algo?
[ ] /dev/urandom for security bits
[ ] research more things to improve!

Stage 4: Attacking algos
[ ] Brute force private key given small pub key
[ ] ...
