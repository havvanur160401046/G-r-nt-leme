# -*- coding: utf-8 -*-
#27.09.2019 Cuma Dersi
#Downsampling m*n -> m/2*n/2 resmi küçültme
#MNIST


#def my_function_1(my_list=[9,3,5,6,2,3,6]):
#    
#    for i in range(len(my_list)):
#        print(i,my_list[i])
#        my_list[i]=my_list[i]+1
#    print(my_list)

#my_function_1(['bir',2,3,4,54,5,56,6]) #hata

#my_function_1([1,2,3,4,54,5,56,6]) 

#my_function_1() 

#import numpy as np
#
#my_list_1=np.array(list([9,3,5,6,2,3,6])) #ndarray
#print(my_list_1)
#print(my_list_1+1)
#
#def my_function_2(my_array=np.array(list([9,3,5,6,2,3,6]))):
#    return my_array-10
#
#my_function_2
import numpy as np
import matplotlib.pyplot as plt

im_1=plt.imread('istanbul.jpg')
plt.imshow(im_1)
plt.show() 

#print(im_1.ndim,im_1.shape)
#im_1=im_1+100
#plt.imshow(im_1)
#plt.show()

def my_f_3(im_100,s=5): #s artım mıktarı
    
    im_1=im_100
    m,n,p=im_1.shape
    im_2=np.zeros((m,n,3),dtype=int)
    #m,n,im_2.shape kontrol için değerler kaybolmuş mu diye

    for m in range (im_1.shape[0]):
        for n in range(im_1.shape[1]):
            im_2[m,n,0]=im_1[m,n,0]-s
            im_2[m,n,1]=im_1[m,n,0]
            im_2[m,n,2]=im_1[m,n,0]

    return im_100

    plt.imshow(im_2)
    plt.show()

def my_f_4(im_500): #s artım mıktarı
    
    m,n,p=im_500.shape
    new_m=int(m/2)
    new_n=int(n/2)
   
    im_600=np.zeros((new_m,new_n),dtype=int)
    #m,n,im_2.shape kontrol için değerler kaybolmuş mu diye

    for m in range (new_m):
        for n in range(new_n):
             s0=(im_500[m*2,n*2,0]+im_500[m*2,n*2,1]+im_500[m*2,n*2,2])/3
#            s0=(im_500[m,n,0]+im_500[m,n,1]+im_500[m,n,2])/3 #bulundugu yerdekı tum rgb degerlerını aldı
            
#            s1=(im_500[m,n+1,0]+im_500[m,n+1,1]+im_500[m,n+1,2])/3 #bir sagdakı
#           
#            s2=(im_500[m+1,n,0]+im_500[m+1,n,1]+im_500[m+1,n,2])/3 #bır soldakı
#            
#            s3=(im_500[m+1,n+1,0]+im_500[m+1,n+1,1]+im_500[m+1,n+1,2])/3 #caprazdakı
            
#            s=(s0+s1+s2+s3)/4
#            im_600[m,n]=int(s)

             im_600[m,n]=int(s0)
             
    return im_600


#im_5=my_f_4(im_1)
#plt.imshow(im_5)
#plt.show()
#plt.imsave("ist_1.jpg",im_5)

im_2=my_f_4(im_1)
plt.imshow(im_2,cmap='gray')
plt.show(im_2)
