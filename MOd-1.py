import hashlib
import os
from docx import document
import docx2txt
from tkinter import *
from tkinter import filedialog
root = Tk()


filename = filedialog.askopenfilename()
text,exe=os.path.splitext(filename)
if exe=='.pdf':
    import PyPDF2
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage()
    readFile=pageObj.extractText()
    print(readFile)
    Hashmsg=hashlib.sha256(readFile.encode()).hexdigest()
    #print (x)
    
if exe=='.docx' :
    my_text = docx2txt.process(filename)
    #print(my_text)
    Hashmsg=hashlib.sha256(my_text.encode()).hexdigest()
    #print (x)
    
if  exe == '.doc' :
    data = open(filename, 'r', encoding="ISO-8859-1").read()
    print(data)
    Hashmsg=hashlib.sha256(data.encode()).hexdigest()
    #print (x)
   

import random
from random import randrange, getrandbits





def is_prim(n, k=128):
    """ Test if a number is prime
        Args:
            n -- int -- the number to test
            k -- int -- the number of tests to do
        return True if n is prime
    """
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True
def generate_prime_candidate(length):
    """ Generate an odd integer randomly
        Args:
            length -- int -- the length of the number to generate, in bits
        return a integer
    """
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p
def generate_prime_number(length=32):
    """ Generate a prime
        Args:
            length -- int -- length of the prime to generate, in          bits
        return a prime
    """
    p = 4
    # keep generating while the primality test fail
    while not is_prim(p, 128):
        p = generate_prime_candidate(length)
    return p








def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
 
def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x % m
 










'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
'''

Euclids extended algorithm for finding the multiplicative inverse of two numbers
'''
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    print("call to multiplicative",d)
    
    if temp_phi == 1:
        return d + phi











 
# Function to return gcd of a and b
def gcd(a, b) :
    if (a == 0) :
        return b
         
    return gcd(b % a, a)
     
 
# Driver Program

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    #n = pq
    n = p * q

    #Phi is the totient of n
    phi = (p-1) * (q-1)

    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)


    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #Use Extended Euclid's Algorithm to generate the private key
    d = modinv(e, phi)

    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    #Unpack the key into it's components
    print("entered encrypt")
    key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]

    #Return the array of bytes
    return cipher

def encrypt1(pk, plaintext):
    #Unpack the key into it's components
    print("entered encrypt")
    key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(char ** key) % n for char in plaintext]

    #Return the array of bytes
    return cipher

def decrypt(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)



def decrypt1(pk, ciphertext):
   #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [(char ** key) % n for char in ciphertext]
    #Return the array of bytes as a string
    return plain
    
    
    
    













    

def main():
    '''
    Detect if the script is being run directly by the user
    '''
    print("RSA Encrypter/ Decrypter")
    p = generate_prime_number(8)
    q = generate_prime_number(8)
    #p1=generate_prime_number(8)
    #q1=generate_prime_number(8)
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    #public1, private1 = generate_keypair(p1, q1)
    print("Your public key is ", public ," and your private key is ", private)
   # print("Your public1 key is ", public1 ," and your private key is ", private1)
    print("if it works")
    message =Hashmsg
    encrypted_msg = encrypt(private, message)
   # encrypted_msg1 = encrypt1(public1, encrypted_msg)
    
    print("Your encrypted message is: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public ," . . .")
    print("Your message is:")
    #decrypted=decrypt1(private1, encrypted_msg1)
    print(decrypt(public, encrypted_msg))
main()


