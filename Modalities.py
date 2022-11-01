from ctypes import sizeof
from sys import getsizeof
import pydicom as dicom
import numpy as np
import matplotlib.pyplot as plt
import os

path=r"C:\Users\Mohamed ElRafie\Downloads\VHF-Head\Head"  #Take the path of the folder that contains the dicom images
ct_images=os.listdir(path)

slices = [dicom.read_file(path+'/'+s,force=True) for s in ct_images]  #find out the slices
#print(slices)


img_shape = list(slices[0].pixel_array.shape)
img_shape.append(len(slices))
volume3d=np.zeros(img_shape)   #create a new array of zeros

for i,s in enumerate(slices):
    array2D=s.pixel_array
    volume3d[:,:,i]= array2D   #Putting the images in a 3D matrix


axial=plt.subplot(2,2,1) #location of plotting
plt.title("Axial")
plt.imshow(volume3d[:,:,img_shape[2]//2])   #showing the axial plane
    

sagital=plt.subplot(2,2,2)   #location of plotting
plt.title("Sagital")
plt.imshow(volume3d[:,img_shape[1]//2,:])    #showing the sagital plane
    

coronal = plt.subplot(2,2,3)    #location of plotting
plt.title("Coronal")
plt.imshow(volume3d[img_shape[0]//2,:,:].T)    #showing the coronal plane
    
plt.show()


print(array2D.shape)
print(volume3d.shape)