import hashlib
import os
from docx import document
import docx2txt
from tkinter import *
from tkinter import filedialog
import pyodbc
def encrypt(pk, plaintext):
    #Unpack the key into it's components
    print("entered encrypt")
    key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]

    #Return the array of bytes
    return cipher

def main():









    root = Tk()

    filename = filedialog.askopenfilename()
    text,exe=os.path.splitext(filename)
    if exe=='.pdf':
        import PyPDF2
        pdfFileObj = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pageObj = pdfReader.getPage(6)
        readFile=pageObj.extractText()
        x=hashlib.sha256(readFile.encode()).hexdigest()
        print (x)
    if exe=='.docx'  :
        my_text = docx2txt.process(filename)
        print(my_text)
        x=hashlib.sha256(my_text.encode()).hexdigest()


    pri1=int(input("enter your private key1"))
    pri2=int(input("enter your private key2"))
    private=(pri1,pri2)
    
    if len(obj)>0:
        message =x
        print(x)
        cypher= encrypt(private, message)
       # encrypted_msg1 = encrypt1(public1, encrypted_msg)
        
        print("Your encrypted message is: ")
        encrypted_msg=':'.join(map(lambda x: str(x), cypher))
        encrypted_msg=encrypted_msg+':'
        print(encrypted_msg)        
main()


    
