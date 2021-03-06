import copy
import math
import random
from numpy import matlib as mb
import cv2
import numpy as np
from PyQt5.QtGui import QPixmap, QImage
from numba import jit


#旋转函数,传入QPixmap返回QPixmap
def rotate(img,angle):
    angle=angle*math.pi/180
    x1=(float)(-(img.width()-1)/2)
    y1=(float)((img.height()-1)/2)
    x2=(float)((img.width()-1)/2)
    y2=(float)((img.height()-1)/2)
    x3=(float)(-(img.width()-1)/2)
    y3=(float)(-(img.height()-1)/2)
    x4=(float)((img.width()-1)/2)
    y4=(float)(-(img.height()-1)/2)

    SinA=(float)(math.sin(angle))
    CosA=(float)(math.cos(angle))
    dx1=CosA*x1+SinA*y1
    dy1=-SinA*x1+CosA*y1
    dx2=CosA*x2+SinA*y2
    dy2=-SinA*x2+CosA*y2
    dx3=CosA*x3+SinA*y3
    dy3=-SinA*x3+CosA*y3
    dx4=CosA*x4+SinA*y4
    dy4=-SinA*x4+CosA*y4

    dWidth=(int)(max(abs(dx4-dx1),abs(dx3-dx2)+0.5))
    dHeight=(int)(max(abs(dy4-dy1),abs(dy3-dy2)+0.5))
    sWidth=img.width()
    sHeight = img.height()


    img.save("temp.jpg")
    img=cv2.imread("temp.jpg")
    dchannel=img.shape[2]

    dimg=np.zeros((dHeight,dWidth,dchannel),dtype=np.uint8)
    vard1=(float)(-0.5*dWidth*CosA-0.5*dHeight*SinA+0.5*sWidth)
    vard2=(float)(0.5*dWidth*SinA-0.5*dHeight*CosA+0.5*sHeight)
    for i in range(dHeight):
        for j in range(dWidth):
            ty = (int)(-j * SinA + i * CosA + vard2 + 0.5)
            tx = (int)(j * CosA + i * SinA + vard1 + 0.5)
            if 0 <= tx < sWidth and 0 <= ty < sHeight:
                for k in range(dchannel):
                    dimg[i,j,k]=img[ty,tx,k]
            else:
                for k in range(dchannel):
                    dimg[i,j,k]=255


    x = dimg.shape[1]#width
    y = dimg.shape[0]#height
    dimg=cv2.cvtColor(dimg,cv2.COLOR_BGR2RGB)
    pix = QPixmap.fromImage(QImage(dimg, x, y,x*dchannel, QImage.Format_RGB888))
    return pix

#缩放函数,sc为缩放系数
@jit(nopython=True)#numba加速
def scale(img_a,Vsc,Hsc):
    height = img_a.shape[0]
    width = img_a.shape[1]
    channel = img_a.shape[2]

    dstheight = (int)(Vsc * height + 0.5)
    dstwidth = (int)(Hsc * width + 0.5)
    dstimage = np.zeros((dstheight, dstwidth, channel), dtype=np.uint8)
    for i in range(dstheight - 1):
        for j in range(dstwidth - 1):
            si = (int)(i * height / dstheight - 1)
            sj = (int)(j * width / dstwidth - 1)
            d1 = ((float)(i + 1) * height / dstheight) - ((int)(i + 1) * height / dstheight)
            d2 = ((float)(j + 1) * width / dstwidth) - ((int)(j + 1) * width / dstwidth)
            for k in range(channel):
                tl = img_a[si, sj, k]
                tr = img_a[si, sj + 1, k]
                bl = img_a[si + 1, sj, k]
                br = img_a[si + 1, sj + 1, k]
                dstimage[i, j, k] = tl * (1 - d1) * (1 - d2) + tr * (d2) * (1 - d1) + bl * (1 - d2) * (d1) + br * (
                    d1) * (d2)
    return dstimage

#水平翻折函数
def HMirror(img):
    img.save("temp.jpg")
    img_a=cv2.imread("temp.jpg")
    height,width,channel=img_a.shape

    dstimage=np.zeros((height,width,channel),dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            for k in range(channel):
                dstimage[i,j,k]=img_a[i,width-1-j,k]
    return dstimage

#垂直翻折函数
def VMirror(img):
    img.save("temp.jpg")
    img_a=cv2.imread("temp.jpg")
    height,width,channel=img_a.shape

    dstimage=np.zeros((height,width,channel),dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            for k in range(channel):
                dstimage[i,j,k]=img_a[height-1-i,j,k]
    return dstimage

#最小边框函数：
def MinBox(img):
    img.save("temp.jpg")
    img_a = cv2.imread("temp.jpg")
    height, width, channel = img_a.shape
    img_g=cv2.cvtColor(img_a,cv2.COLOR_BGR2GRAY)
    _,img_g = cv2.threshold(img_g, 250, 255, cv2.THRESH_BINARY_INV)
    x,y=np.nonzero(img_g)#x为行y为列
    dstheight=max(x)-min(x)
    dstwidth=max(y)-min(y)

    dstimage = np.zeros((dstheight, dstwidth, channel), dtype=np.uint8)
    dstimage[:,:,:]=img_a[min(x):min(x)+dstheight,min(y):min(y)+dstwidth,:]
    return dstimage

#裁剪图像函数:
def imgcut(img,x,y,h,w):
    newimg=img[x:w,y:h,:]
    return newimg

#亮度调整
def Vchange(img,V):
    img.save("temp.jpg")
    img_a=cv2.imread("temp.jpg")
    cv2.convertScaleAbs(img_a,img_a,1,V)
    return img_a

#饱和度调整
def Schange(img,S):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    img=Schange_process(img,S)
    img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
    return img
#饱和度调整过程：单独写遍历函数以获取numba库加速
@jit(nopython=True)#numba加速
def Schange_process(img,S):
    height,width,channel=img.shape[0],img.shape[1],img.shape[2]
    for i in range(height):
        for j in range(width):
            if img[i,j,1]>=128:
                img[i,j,1]-=S
            elif img[i,j,1]<128:
                img[i,j,1]+=S
    return img

#色相调整
def Hchange(img,G):
    img=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)

    img[:,:,0]+=G
    img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
    return img


#对比度调整
def Cchange(img,C):
    cv2.convertScaleAbs(img,img,(100-C)*0.01,0)
    return img

#Roberts算子
@jit(nopython=True)
def sharpen_Roberts(img,L):
    height = img.shape[0]
    width = img.shape[1]
    channel = img.shape[2]

    img_copy = img
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            for k in range(channel):
                x = img_copy[i, j, k] -img_copy[i+1,j+1,k]
                y = img_copy[i + 1, j,k]-img_copy[i,j+1,k]
                t = int(math.sqrt(x * x + y * y) + 0.5)
                if t > 255: t = 0
                img[i, j, k] +=L*t
    return img

#Prewitt算子
@jit(nopython=True)
def sharpen_Prewitt(img,L):
    height = img.shape[0]
    width = img.shape[1]
    channel = img.shape[2]

    img_copy = img
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            for k in range(channel):
                x = img_copy[i + 1, j + 1, k] + img_copy[i, j + 1, k] + img_copy[i - 1, j + 1, k] - \
                    (img_copy[i + 1, j - 1, k] + img_copy[i, j - 1, k] + img_copy[i - 1, j - 1, k])
                y = img_copy[i - 1, j - 1, k] + img_copy[i - 1, j, k] + img_copy[i - 1, j + 1, k] - \
                    (img_copy[i + 1, j - 1, k] + img_copy[i + 1, j, k] + img_copy[i + 1, j + 1, k])
                t = int(math.sqrt(x * x + y * y) + 0.5)
                if t > 255: t = 0
                img[i, j, k]+=L*t
    return img

#Sobel算子
@jit(nopython=True)
def sharpen_Sobel(img,L):
    height=img.shape[0]
    width=img.shape[1]
    channel=img.shape[2]

    img_copy=img
    for i in range(1,height-1):
        for j in range(1,width-1):
            for k in range(channel):
                x=img_copy[i-1,j+1,k]+2*img_copy[i,j+1,k]+img_copy[i+1,j+1,k]-\
                  (img_copy[i - 1, j - 1, k]+2*img_copy[i,j-1,k]+img_copy[i+1,j-1,k])
                y=img_copy[i-1,j-1,k]+2*img_copy[i-1,j,k]+img_copy[i-1,j+1,k]- \
                  (img_copy[i + 1, j - 1, k]+2*img_copy[i+1,j,k]+img_copy[i+1,j+1,k])
                t=int(math.sqrt(x*x+y*y)+0.5)
                if t>255:t=0
                img[i,j,k]+=L*t
    return img

#Laplacian算子
@jit(nopython=True)
def sharpen_Laplacian(img,L):
    height = img.shape[0]
    width = img.shape[1]
    channel = img.shape[2]

    img_copy = img
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            for k in range(channel):
                t = img_copy[i + 1, j, k] +img_copy[i-1, j, k] + img_copy[i, j + 1, k] + \
                    img_copy[i, j - 1, k] -4* img_copy[i, j, k]
                if t < 0: t = 0
                img[i, j, k] +=L*t
    return img

#椒盐噪声
def noise_SP(img,SNR):
    height=img.shape[0]
    width=img.shape[1]
    num=height*width*(1-SNR)
    for i in range(int(num)):
        x=random.randint(0,height-1)
        y=random.randint(0,width-1)
        v=random.choice([0,255])
        img[x,y,:]=v

    return img

#高斯噪声
def noise_Gauss(img,mu,sigma):
    height=img.shape[0]
    width=img.shape[1]
    channel=img.shape[2]

    for i in range(height):
        for j in range(width):
            for k in range(channel):
                img[i,j,k]+=np.random.normal(mu,sigma,1)
                if img[i,j,k]>255:
                    img[i,j,k]=0

    return img

#均匀随机噪声
def noise_UR(img,low,hig,rate):
    height=img.shape[0]
    width=img.shape[1]
    channel=img.shape[2]
    num=int(rate*height*width)
    for i in range(num):
        x=random.randint(0,height-1)
        y=random.randint(0,width-1)
        for k in range(channel):
            img[x,y,k]+=np.random.uniform(low,hig,1)

    return img

#均值滤波
def filter_mean(img,size):
    kernel=np.full((size,size),float(1)/(size*size),dtype="float32")
    img = cv2.filter2D(img, -1, kernel)
    return img

def spilt( a ):
    if a%2 == 0:
        x1 = x2 = a/2
    else:
        x1 = math.floor( a/2 )
        x2 = a - x1
    return -x1,x2

def original (i, j, k,a, b,img):
    x1, x2 = spilt(a)
    y1, y2 = spilt(b)
    temp = np.zeros(a * b)
    count = 0
    for m in range(x1, x2):
        for n in range(y1, y2):
            if i + m < 0 or i + m > img.shape[0] - 1 or j + n < 0 or j + n > img.shape[1] - 1:
                temp[count] = img[i, j, k]
            else:
                temp[count] = img[i + m, j + n, k]
            count += 1
    return  temp

#中值滤波
def filter_mid(img,size):
    img0 = copy.copy(img)
    for i in range(0, img.shape[0]):
        for j in range(2, img.shape[1]):
            for k in range(img.shape[2]):
                temp = original(i, j, k, size, size, img0)
                img[i, j, k] = np.median(temp)

    cv2.imshow("res",img)
    cv2.waitKey(0)
    return img

#最大值滤波
def filter_max(img,size):
    img0 = copy.copy(img)
    for i in range(0, img.shape[0]):
        for j in range(2, img.shape[1]):
            for k in range(img.shape[2]):
                temp = original(i, j, k, size, size, img0)
                img[i, j, k] = np.max(temp)

    cv2.imshow("res",img)
    cv2.waitKey(0)
    return img

#最小值滤波
def filter_min(img,size):
    img0 = copy.copy(img)
    for i in range(0, img.shape[0]):
        for j in range(2, img.shape[1]):
            for k in range(img.shape[2]):
                temp = original(i, j, k, size, size, img0)
                img[i, j, k] = np.min(temp)

    cv2.imshow("res",img)
    cv2.waitKey(0)
    return img

#轮廓提取
def contour_get(img):
    kernel = np.array((
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1]), dtype="float32")
    img = cv2.filter2D(img, -1, kernel)
    return img

#浮雕效果
def emboss_get(img):
    kernel = np.array((
        [-2, -1, 0],
        [-1, 1, 1],
        [0, 1, 2]), dtype="float32")
    img = cv2.filter2D(img, -1, kernel)
    return img

#鱼眼效果
def fisheye_get(img):
    row = img.shape[0]
    col = img.shape[1]
    channel = img.shape[2]
    new_img = np.zeros([row, col, channel], dtype=np.uint8)
    center_x = row / 2
    center_y = col / 2
    radius = min(center_x, center_y)
    for i in range(row):
        for j in range(col):

            distance = ((i - center_x) * (i - center_x) + (j - center_y) * (j - center_y))
            new_dist = math.sqrt(distance)
            new_img[i, j, :] = img[i, j, :]
            if distance <= radius ** 2:
                new_i = np.int(np.floor(new_dist * (i - center_x) / radius + center_x))
                new_j = np.int(np.floor(new_dist * (j - center_y) / radius + center_y))
                new_img[i, j, :] = img[new_i, new_j, :]
    return new_img

#素描黑白
def sketchbk_get(img):
    cartoon_image1, cartoon_image2 = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.5, shade_factor=0.02)
    return cartoon_image1

#素描彩色
def sketchcl_get(img):
    cartoon_image1, cartoon_image2 = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.5, shade_factor=0.02)
    return cartoon_image2


#卡通化风格一
def cartoon1_get(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 7)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10)
    # Making a Cartoon of the image
    color = cv2.bilateralFilter(img, 12, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    # Visualize the cartoon image
    return cartoon

#卡通化风格二
def cartoon2_get(img):
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # apply gaussian blur
    grayImage = cv2.GaussianBlur(grayImage, (3, 3), 0)
    # detect edges
    edgeImage = cv2.Laplacian(grayImage, -1, ksize=5)
    edgeImage = 255 - edgeImage
    # threshold image
    ret, edgeImage = cv2.threshold(edgeImage, 150, 255, cv2.THRESH_BINARY)
    # blur images heavily using edgePreservingFilter
    edgePreservingImage = cv2.edgePreservingFilter(img, flags=2, sigma_s=50, sigma_r=0.4)
    # create output matrix
    output = np.zeros(grayImage.shape)
    # combine cartoon image and edges image
    output = cv2.bitwise_and(edgePreservingImage, edgePreservingImage, mask=edgeImage)

    return output

#卡通化风格三
def cartoon3_get(img):
    cartoon_image = cv2.stylization(img, sigma_s=150, sigma_r=0.25)
    return cartoon_image
