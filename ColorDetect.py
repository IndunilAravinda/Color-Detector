import cv2
import numpy as np

def main():

   cap = cv2.VideoCapture(0)

   if cap.isOpened():
       ret,fram = cap.read()
       print(ret)
   else:
       ret = False

   while ret:
       ret,fram = cap.read()
       hsv = cv2.cvtColor(fram,cv2.COLOR_BGR2HSV)

##############################################################       

       #blue color
       low = np.array([100,10,50])
       high = np.array([140,255,255])

       img_mask = cv2.inRange(hsv, low, high)
       outputs = cv2.bitwise_and(fram,fram, mask=img_mask)

       #para 1 source, para 2 output , para 3 threshold mask 
       
       #bitwise_and=Calculates the per-element bit-wise conjunction of two arrays or an array and a scalar.
       #Result is true only if both operands are true. It can be used to set up a mask to check the values of certain bits.

       cv2.imshow("orginal immages" , fram)
       cv2.imshow('filter orginals' , outputs)

       print(outputs.mean())

       if(outputs.mean()>20):
          print("BLUE "+str(outputs.mean()))
       else:
          print("Searching")

################################################################
          
       #red color
       low = np.array([0,10,50])
       high = np.array([0,255,255])

       img_mask = cv2.inRange(hsv, low, high)
       output = cv2.bitwise_and(fram,fram, mask=img_mask)

       cv2.imshow("orginal immage" , fram)
       cv2.imshow('filter orginal' , output)

       if(output.mean()>0.2):
          print("RED "+str(output.mean()))
       else:
          print("")

##################################################################

       cv2.waitKey(1000)

main()
