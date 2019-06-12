from tkinter import *
from tkinter import filedialog
import tkinter as tk
import hashlib
import os
from docx import document
import docx2txt
from tkinter import *
from tkinter import filedialog
import defi
def decrypt(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)

def encrypt(pk, plaintext):
    #Unpack the key into it's components
    print("entered encrypt")
    key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]

    #Return the array of bytes
    return cipher
def ds1():
    root1 = Toplevel()
    root1.title("HOME")
    root1.geometry('3500x2000')
    menu = Menu(root1)
    root1.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu )
    filemenu.add_command(label="Register",command=Registration)
    filemenu.add_command(label="Forgot Keys",command=About)
    filemenu.add_command(label="Quit",command=qui)
    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=About)

    frame = tk.Frame(root1)
    frame.pack()

    button = tk.Button(frame, 
                       text="Send A File", 
                       fg="red",
                       command=send)
    button.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                       text="Check A File",
                       command=check)
    slogan.pack(side=tk.LEFT)
def check():
    win = Toplevel()
    # entry boxes put in a frame, text stored in variables k, l
    ent_frame = Frame(win)
    Label(ent_frame, text="Enter Public Key").pack(side=LEFT)
    k1 = Entry(ent_frame, width=15)
    k1.pack(side=LEFT)
    k2 = Entry(ent_frame, width=15)
    k2.pack(side=LEFT)
    Label(ent_frame, text="Enter Private Key").pack(side=LEFT)
    l1 = Entry(ent_frame, width=15)
    l1.pack(side=LEFT)
    l2 = Entry(ent_frame, width=15)
    l2.pack(side=LEFT)
    Label(ent_frame, text="Enter Path Of Cypher Text").pack(side=LEFT)
    l3 = Entry(ent_frame, width=15)
    l3.pack(side=LEFT)
    
    ent_frame.pack()
    def had():
        filename = filedialog.askopenfilename()
        text,exe=os.path.splitext(filename)
        if exe=='.pdf':
            import PyPDF2
            pdfFileObj = open(filename, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            pageObj = pdfReader.getPage(6)
            readFile=pageObj.extractText()
            x=hashlib.sha256(readFile.encode()).hexdigest()
            #print (x)
        if exe=='.docx'  :
            my_text = docx2txt.process(filename)
            x=hashlib.sha256(my_text.encode()).hexdigest()
        pub1=k1.get()
        pub2=l1.get()
        obj=2
        #pub1=int(input("enter your public key1"))
        #pub2=int(input("enter your public key2"))
        public=(pub1,pub2)
        #conn=pyodbc.connect("DRIVER={SQL Server};server=localhost;database=Digital_Signature")
        #cur=conn.execute("select User_id from User_info where public_key1={} and public_key2={}".format(pub1,pub2))
        #obj=cur.fetchone()
        if obj>0:
            message =x
            #print(x)
            
            cypher=l3.get()
            msg=''
            encrypted_msg=[]
            for char in cypher:
                if char is ':':
                    con_msg=int(msg)
                    encrypted_msg.append(con_msg)
                    msg=''
                else:
                    msg+=char
                
            print("Decrypting message with public key ", public ," . . .")
            decrypted_msg=decrypt(public, encrypted_msg)
            print(type(decrypted_msg))
            print(type(x))
            
            if str(decrypted_msg)==x:
                Label(ent_frame, text="file send matches with file received").pack(side=LEFT)
                print("file send matches with file received")
                Label(ent_frame, text="Your message is:").pack(side=LEFT)
                print("Your message is:")
                val=0
          #  decrypted=decrypt1(private1, encrypted_msg1)
                print(decrypted_msg)
                Label(ent_frame, text=decrypted_msg).pack(side=LEFT)
            def compare() :
                win.destroy()
                win = Toplevel()
    
                ent_frame = Frame(win)
                if(val==0):
                    Label(ent_frame, text="Files Matched").pack(side=LEFT)
                else :
                     Label(ent_frame, text="Files Not Matched").pack(side=LEFT)
            Button(win, text="compare" ,command=compare).pack(side=BOTTOM)
                
    Button(win, text="decrypt",command=had).pack(side=BOTTOM)
def send():
    root1 = Toplevel()
    root1.title("SEND")
    root1.geometry('3500x2000')
    menu = Menu(root1)
    root1.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu )
    filemenu.add_command(label="Register",command=Registration)
    filemenu.add_command(label="Forgot Keys",command=About)
    filemenu.add_command(label="Quit",command=qui)
    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=About)
    frame = tk.Frame(root1)
    
    # entry boxes put in a frame, text stored in variables k, l
    ent_frame = Frame(root1)
    Label(ent_frame, text="Private Key").pack(side=LEFT)
    q1 = Entry(ent_frame, width=15)
    q1.pack(side=LEFT)
    Label(ent_frame, text="Public Key").pack(side=LEFT)
    r1 = Entry(ent_frame, width=15)
    r1.pack(side=LEFT)
    ent_frame.pack()
    def submit():
        filename = filedialog.askopenfilename()
       
        text,exe=os.path.splitext(filename)
        if exe=='.pdf':
            import PyPDF2
            pdfFileObj = open(filename, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            pageObj = pdfReader.getPage(6)
            count=1
            readFile=pageObj.extractText()
            x=hashlib.sha256(readFile.encode()).hexdigest()
            
        if exe=='.docx'  :
            my_text = docx2txt.process(filename)
            
            count=1
            x=hashlib.sha256(my_text.encode()).hexdigest()
        else :
            Label(ent_frame, text="cannot encrypt other than .docx and .pdf").pack(side=LEFT)
            print("cannot encrypt other than .docx and .pdf")
            count=0
        if(count==1):
            pri1=int(q1.get())
            pri2=int(r1.get())
            print(pri1)
            #pri1=int(input("enter your private key1"))
            #pri2=int(input("enter your private key2"))
            private=(pri1,pri2)
            #conn=pyodbc.connect("DRIVER={SQL Server};server=localhost;database=Digital_Signature")
            #cur=conn.execute("select User_id from User_info where private_key={} and private_key2={}".format(pri1,pri2))
            #obj=cur.fetchone()
            if len(private)>0:
                message =x
                
                cypher= encrypt(private, message)
               # encrypted_msg1 = encrypt1(public1, encrypted_msg)
                
                print("Your encrypted message is: ")
                encrypted_msg=':'.join(map(lambda x: str(x), cypher))
                encrypted_msg=encrypted_msg+':'
                Label(ent_frame, text=encrypted_msg).pack(side=LEFT)
                print(encrypted_msg)

    Button(root1, text="Submit",command=submit).pack(side=LEFT)
    
      
def ds():
    
    menu = Toplevel()
    # entry boxes put in a frame, text stored in variables k, l
    frame= Frame(menu)
    frame.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu )
    filemenu.add_command(label="Register",command=Registration)
   
    filemenu.add_command(label="Forgot Keys",command=About)
    filemenu.add_command(label="Quit",command=qui)
    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=About)
    
    
    
    frame.pack()
    lbl_pubkey = Label(frame, text = "Public Key:", font=('arial', 7), bd=15)
    lbl_pubkey.grid(row=0, sticky="e")
    
    btn_log = Button(frame, text = "Choose", width=15,command=choose)
    btn_log.grid(pady=2, row=2, columnspan=1)
    
    lbl_text = Label(frame)
    lbl_text.grid(row=2, columnspan=2)
    
    Button(frame, text="Save",command=SaveIt).pack(side=BOTTOM)
  
def Registration():

    win = Toplevel()
    # entry boxes put in a frame, text stored in variables k, l
    ent_frame = Frame(win)
    Label(ent_frame, text="User Name").pack(side=LEFT)
    k1 = Entry(ent_frame, width=15)
    k1.pack(side=LEFT)
    Label(ent_frame, text="Email").pack(side=LEFT)
    l1 = Entry(ent_frame, width=15)
    l1.pack(side=LEFT)
    Label(ent_frame, text="Phone Number").pack(side=LEFT)
    q1 = Entry(ent_frame, width=15)
    q1.pack(side=LEFT)
    Label(ent_frame, text="Password").pack(side=LEFT)
    r1 = Entry(ent_frame, width=15)
    r1.pack(side=LEFT)
    ent_frame.pack()
    # using get method for entry boxes above
    def SaveIt():
        name = k1.get()
        email = l1.get()
        number = q1.get()
        password = r1.get()
        p = generate_prime_number(8)
        q = generate_prime_number(8)
        public, private = generate_keypair(p, q)
        public1,public2=public
        private1,private2=private
        #conn=pyodbc.connect("DRIVER={SQL Server};server=localhost;database=Digital_Signature") 
        #conn.execute("Insert into User_info values(?,?,?,?,?,?,?,?,?,?)",(name,email,number,password,p,q,public1,public2,private1,private2))
        #conn.commit()
        #g=conn.execute("select User_id from User_info where public_key1={} and public_key2={} and private_key={} and private_key2={}".format(public1,public2,private1,private2))
        #g.fetchone()
        #print("your id is ",g[0])
        if(name=='null'):
           print("fill out form feilds") 
        else:
            Label(ent_frame, text="Public Key").pack(side=LEFT)
            Label(ent_frame, text="Private Key").pack(side=LEFT)
            Label(ent_frame, text=public).pack(side=BOTTOM)
            Label(ent_frame, text=private).pack(side=LEFT)
            print("your public key is ",public)
            print("your private key is ",private)
            #win.destroy()
    Button(win, text="Save",command=SaveIt).pack(side=BOTTOM)

import pyodbc
import random
from random import randrange, getrandbits
import pyodbc

def is_prim(n, k=128):
    """ Test if a number is prime
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


# Function to return gcd of a and b
def gcd(a, b) :
    if (a == 0) :
        return b
         
    return gcd(b % a, a)
     
 
# Driver Program
'''
Tests to see if a number is prime.
'''
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



   













def qui():
    root.destroy()
def About():
    print ("This is a simple example of a menu")
def choose():
        filename = filedialog.askopenfilename()
        text,exe=os.path.splitext(filename)
        return exe,filename

root = Tk()
root.title("HOME")
root.geometry('3500x2000')
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu )
filemenu.add_command(label="Register",command=Registration)
filemenu.add_command(label="Forgot Keys",command=About)
filemenu.add_command(label="Quit",command=qui)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="Generate Digital Signature", 
                   fg="red",
                   command=Registration)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Use Digital Signature",
                   command=ds1)
slogan.pack(side=tk.LEFT)

root.mainloop()


