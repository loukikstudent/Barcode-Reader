import numpy as np
import matplotlib.pyplot as plt
import sqlite3
from pyzbar import pyzbar
import argparse
import cv2
##ap = argparse.ArgumentParser()
##ap.add_argument("-i", "--image", required=True,help="path to input image")
##args = vars(ap.parse_args())
# load the input image
##image = cv2.imread("qr code.png")
cap = cv2.VideoCapture(0)
#to output the file
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out=cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
def some():
     while True:
          ret, frame = cap.read()
          #gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
          #out.write(frame)
          cv2.imshow('frame',frame)
          #cv2.imshow('gray',gray)
          if cv2.waitKey(1) & 0xFF == ord('q'):
               break
          # find the barcodes in the image and decode each of the barcodes
          barcodes = pyzbar.decode(frame)
          if barcodes:
                  break

     #cap.release()
     #out.release()
     cv2.destroyAllWindows()
     # loop over the detected barcodes
     for barcode in barcodes:
             # the barcode data is a bytes object so if we want to draw it on
             # our output image we need to convert it to a string first
             barcodeData = barcode.data.decode("utf-8")
             barcodeType = barcode.type             
             # print the barcode type and data to the terminal
             print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
             print ("For More Information type y/n")
             a=input()
             if (a=="y"):
                     conn=sqlite3.connect('test.sqlite')
                     cur=conn.cursor()
                     data=barcodeData.split('\n')
                     idn=data[0].split(":")
                     idn[1]=idn[1].lstrip()
                     #print(idn)
                     cur.execute('SELECT field2 FROM test1 WHERE ID=( ? )',(idn[1],) )
                     row=cur.fetchone()
                     for line in row:
                             print (line)
some()
while True:
     print("Read more")
     n=input()
     if (n=='y'):
          some()
     else:
          cap.release()
          break
                

