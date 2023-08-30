import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,writers
import numpy as np
import math

plt.subplot(1,2,1)
plt.title("anim plot")
x2=[]
def ani(i):
    x2.append(i/100)
    #plt.clf()
    plt.plot(x2,x2)
    plt.xlim(0,10)
    plt.ylim(0, 10)

#anim=FuncAnimation(plt.gcf(),ani,interval=10)
for i in range(1000):
    ani(i)

plt.subplot(1,2,2)
plt.title("anim plot")
"""x2=[]
def ani(i):
    x2.append(i/10)
    plt.clf()
    plt.plot(x2,x2)
    plt.xlim(0,10)
    plt.ylim(0, 10)

anim=FuncAnimation(plt.gcf(),ani,interval=10)
"""

lim=10*np.pi
llim=0
len=5000
theeta1=np.linspace(llim,lim,len)

def din(fx, xx, l1, l2):
    l1 += llim
    l2 += llim
    a = math.ceil(l1 / (xx[1] - xx[0]))
    b = math.ceil(l2 / (xx[1] - xx[0]))
    y1 = np.cumsum(fx[a:b])
    y2 = y1[b - a - 1] * (xx[1] - xx[0])
    return y2

wfx1=2
wfx2=3
wfx3=5
a1=1
a2=1
a3=1

fx = np.sin(wfx1 * theeta1)+np.sin(wfx2* theeta1)+np.sin(wfx3* theeta1)+a1+a2+a3

def ani(i):
    x2.append(i/10)
    plt.clf()
    plt.plot(x2,x2)
    plt.xlim(0,10)
    plt.ylim(0, 10)

darrs = np.linspace(0,0,len)
darrc = np.linspace(0,0,len)

for i in range(len):
    darrs[i]=din(fx*np.sin(theeta1[i]*theeta1),theeta1,0,lim)*2/lim
    darrc[i]=din(fx*np.cos(theeta1[i]*theeta1),theeta1,0,lim)*2/lim

limits = 10
sp=2
def animation(i):
    i=2*i
    plt.clf()
    plt.xlim(-4/3*limits, 4/3*limits)
    plt.ylim(-limits, limits)
    plt.grid()
    y1 = np.e ** (1j * theeta1[i] * theeta1)
    y2 = y1 * fx
    plt.plot(y2.real, y2.imag,linewidth=1)
    w1 = theeta1[i]
    plt.plot(wfx1, 0, 'g', marker='*',markersize=3)
    plt.plot(wfx2, 0, 'g', marker='*',markersize=3)
    plt.plot(wfx3, 0, 'g', marker='*',markersize=3)
    plt.plot(theeta1, darrs, linewidth=0.5)
    plt.plot(w1, 0, 'b', marker='*',markersize=3)
    plt.plot(darrc[i], darrs[i], 'brown', marker='*',markersize=3)
    ax = plt.gca()
    ax.set_aspect('equal')

anim = FuncAnimation(plt.gcf(),animation,frames=int(len/8),interval=66)

#To save this animation as mp4

Writer=writers['ffmpeg']
writer=Writer(fps=15,metadata={'artist':'Me'},bitrate=2700)#dpi*18
anim.save('MyFirstAnim.mp4',writer,dpi=150)#dpi=resolution/4.8

plt.show()