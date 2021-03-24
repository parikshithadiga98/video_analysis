#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
url="http://192.168.1.3:8080/video"


# In[2]:


cp=cv2.VideoCapture(url)


# In[3]:


while(True):
    ret,frame=cp.read()
    if frame is not None:
        cv2.imshow("frame",frame)
    q=cv2.waitKey(1)
    if q==ord("q"):
        break
cv2.destroyAllWindows()


# In[ ]:




