import os 
import cv2 as cv
import numpy as np

people=['Barack Obama',"Michelle Obama","Paul Kagame"]

p=[]

for i in os.listdir(r'C:\Users\Prett\Documents\learn\pyOpen\faces'):
    p.append(i)

print(p)

