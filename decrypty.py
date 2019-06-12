import hashlib
import os
from docx import document
import docx2txt
from tkinter import *
from tkinter import filedialog
import pyodbc

def decrypt(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)

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
        x=hashlib.sha256(my_text.encode()).hexdigest()

    pub1=int(input("enter your public key1"))
    pub2=int(input("enter your public key2"))
    public=(pub1,pub2)
    conn=pyodbc.connect("DRIVER={SQL Server};server=localhost;database=Digital_Signature")
    cur=conn.execute("select User_id from User_info where public_key1={} and public_key2={}".format(pub1,pub2))
    obj=cur.fetchone()
    if len(obj)>0:
        message =x
        print(x)
        cypher=input("Enter encrypted msg")
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
            print("file send matches with file received")
            print("Your message is:")
      #  decrypted=decrypt1(private1, encrypted_msg1)
            print(decrypted_msg)
main()


    
