

PROCESS

A
- generate two random primes roughly the same size, `p1` and `p2`
- multiply the two to get `n`
- calculate phi(n) (easy)
- picks small odd number e which does not share factor with n
- private exponent d = (2*phi(n)+1)/e
- n and e are public key
- 

B:
- creates ciphertext by calculating message^(e) mod (n)

A:
- decrypts with: c^(d) mod n = cleartext

***

- euler's totient phi(n) = number of integers <= n, not sharing common factors with n
	- hence phi(`prime`) = `prime-1`
	- phi(`n`) = phi(`p``) * phi(`p2`)

- euler's theorem


Paper

- background info
	- background to the problem
		- the problem of key distribution
			- most encryption e.g. one time pads good in theory, but still need to distribute keys -- vulnerable
			- what if you could communicate over a public channel without sharing secrets beforehand?
				- one approach diffie-helman key exchange
				- asymmetric public/private key encryption another
	- history
		- initial gchq discovery
			- not really used to public knowledge
		- later discovery by Ron Rivest, Adi Shamir, and Leonard Adleman
			- attempts over some years to create a suitable trapdoor function
		- published in 1977
	- use and importance
		- extremely widespread
		- ssh, 
- description of rsa algorithm
	- focus on intuitive understanding
	- also make sure it's technically detailed
	- examples and diagrams
- discusion of relative strengths and weaknesses
	- attacks on rsa
		- integer factorisation
		- faulty key generation
		- weaknesses in randon number generation
	- performance/size relative to other algos
		- compare to contemporaries e.g. ed25519
	- safety into the future
		- what key size?
			- 2048 no longer safe?
		- quantum?

***

comment on numberphile RSA vid:

"RSA's exponent of 65537 is chosen because it is a) prime and b) 2^16 + 1 which is 10000000000000001 binary. This makes modular exponentiation very much faster without sacrificing security. We find e and d mod (p - 1)(q - 1) because that is how modular multiplicative inverses work. Out exponent e must be coprime to (p - 1)(q - 1) but it is very unlikely that if we choose e prime, a randomly chosen p and q will yield either p - 1 or q - 1 as a multiple of e. If we are unlucky, we just choose new primes. There are other factors in the choice of p and q that must be taken into consideration, such that even though they should be roughly the same size, they shouldn't be too close to sqrt(n) i.e. if you want a 2048 bit modulus, don't make both p and q be 1024 bits."

