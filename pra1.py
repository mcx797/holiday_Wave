import numpy as np
from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt
import seaborn


#采样点选择1400个，因为设置的信号频率分量最高为600Hz，根据采样定理知采样频率要大于信号频率2倍，所以这里设置采样频率为1400Hz（即一秒内有1400个采样点）
x=np.linspace(0,1,200)

#设置需要采样的信号，频率分量有180，390和600
#y=7*np.sin(2*np.pi*180*x) + 1.5*np.sin(2*np.pi*390*x)+5.1*np.sin(2*np.pi*600*x)
y = [490, 477, 467, 458, 450, 442, 433, 426, 419, 413, 411, 428, 445, 441, 434, 436, 446, 442, 427, 414, 402,
         391, 381, 372, 366, 363, 363, 364, 366, 372, 382, 397, 414, 430, 444, 460, 481, 502, 522, 539, 551, 561,
         567, 569, 568, 566, 570, 576, 578, 574, 565, 553, 541, 529, 519, 507, 496, 486, 494, 528, 551, 563, 576,
         596, 612, 624, 631, 636, 639, 640, 640, 638, 635, 633, 630, 625, 620, 615, 609, 603, 597, 590, 584, 578,
         571, 559, 541, 529, 524, 511, 486, 454, 422, 394, 372, 348, 340, 335, 334, 332, 332, 332, 332, 332, 333,
         336, 339, 341, 344, 349, 355, 360, 366, 372, 383, 396, 408, 419, 432, 448, 463, 473, 482, 493, 511, 530,
         551, 568, 580, 595, 597, 597, 595, 593, 598, 606, 619, 632, 642, 653, 659, 658, 653, 645, 640, 641, 643,
         650, 656, 659, 659, 655, 649, 640, 632, 626, 621, 614, 603, 590, 575, 564, 550, 530, 519, 507, 495, 484,
         472, 462, 452, 445, 437, 430, 423, 417, 423, 442, 445, 435, 423, 422, 431, 436, 428, 413, 401, 390, 381,
         373, 367, 363, 364, 365, 367, 371, 378, 396, 411, 428]
yy=fft(y)                     #快速傅里叶变换
yreal = yy.real               # 获取实数部分
yimag = yy.imag               # 获取虚数部分

yf=abs(fft(y))                # 取模
yf1=abs(fft(y))/((len(x)/2))           #归一化处理
yf2 = yf1[range(int(len(x)/2))]  #由于对称性，只取一半区间

xf = np.arange(len(y))        # 频率
xf1 = xf
xf2 = xf[range(int(len(x)/2))]  #取一半区间

#原始波形
plt.subplot(221)
plt.plot(x[0:50],y[0:50])
plt.title('Original wave')
#混合波的FFT（双边频率范围）
plt.subplot(222)
plt.plot(xf,yf,'r') #显示原始信号的FFT模值
plt.title('FFT of Mixed wave(two sides frequency range)',fontsize=7,color='#7A378B')  #注意这里的颜色可以查询颜色代码表
#混合波的FFT（归一化）
plt.subplot(223)
plt.plot(xf1,yf1,'g')
plt.title('FFT of Mixed wave(normalization)',fontsize=9,color='r')

plt.subplot(224)
plt.plot(xf2,yf2,'b')
plt.title('FFT of Mixed wave)',fontsize=10,color='#F08080')


plt.show()