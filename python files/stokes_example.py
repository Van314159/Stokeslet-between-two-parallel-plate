# In fact, hankel funciton can be imported by scipy.
# That maybe faster.
# z(m) is the m-th root of sinh(z)**2 = z**2 
# pre-calculate pi first.
import mpmath as mp
import numpy as np
from mpmath import sinh, cosh, sqrt
import time as time
import os as os
os.chdir("D:\\Sync Work\\Code\\")
import stokes_main as skm
import stokes_ as sk
%matplotlib inline
mp.dps = 30
mp.pretty = True

'''Step 1: 准备工作'''
pi = mp.pi
zm_list = np.load('zm_list.npy')
zm = lambda n: zm_list[int(n-1)]

'''Step 2: 定义常用的函数'''
def sinsin(n, x3, h, H):
    return sin((n*pi*h)/H) * sin((n*pi*x3)/H)
        
def shsh(m, x3, h, H):
    return 1/zm(m) * sinh((zm(m)*x3)/H) * sinh((zm(m)*h)/H)

def chsh(m, x3, h, H):
    return x3/H * cosh((zm(m)*x3)/H)*sinh((zm(m)*h)/H)
    
def shch(m, x3, h, H):
    return h/H * sinh((zm(m)*x3)/H)*cosh((zm(m)*h)/H)
    
def chMinsh(m, x3, h, H): 
    return sqrt(1+zm(m)**2) * cosh((zm(m)*(x3 + h))/H) - zm(m)*sinh((zm(m)*(h + x3))/H)
    
def inverseOfzm_Min(n):
    return 1 / (sqrt(1+zm(n)**2)-1)

def zm_Add(n):
    return (sqrt(1+zm(n)**2)+1)

'''Step 3: 定义速度函数 u33'''    
def u33(r, x3, h, H, n): 
    return -pi/H * mp.im((zm(n)* mp.hankel1(0, (r*zm(n))/H)) * inverseOfzm_Min(n) *
         (zm_Add(n) * (chsh(n, x3, h, H) + shch(n, x3, h, H) - shsh(n, x3, h, H))
        - (h*x3) / (H**2) * zm(n) * (chMinsh(n, x3, h, H) + cosh((x3 - h)*zm(n)/H))
        - zm(n)**2 * (x3 + h) / H * shsh(n, x3, h, H)))
		
'''Step 4: 给定参数'''
'''
small_r_near_z: r = 0.01H, z = 1.01h, h = 1.0, H = 4.0
large_r_near_z: r = H,     z = 1.01h, h = 1.0, H = 4.0
small_r_far_z:  r = 0.01H, z = 2.0 h, h = 1.0, H = 4.0
large_r_far_z:  r = H,     z = 2.0 h, h = 1.0, H = 4.0
'''
h = 1.0
H = 4.0
small_r_near_r = [0.01*H, 1.01*h, h, H]
large_r_near_z = [1*H, 1.01*h, h, H]
small_r_far_z  = [0.01*H, 2.0*h, h, H]
large_r_far_z  = [1*H, 2.0*h, h, H]

'''Step 5: 计算积分法和级数法.'''

'''项数列表: 从 1 到 20.'''
n_series = np.arange(5, 20)

'''积分法求解 u33'''
start = time.clock()
u33_quad = sk.u33(0, *large_r_far_z)
end = time.clock()
t_quad = start - end

'''级数法求解 u33'''
u33_series = []
t_series = []
for n in n_series:
    start = time.clock()
    u33_series_atom = mp.nsum(lambda m: u33(*large_r_far_z, m),[1, n])
    u33_series.append(abs((u33_series_atom-u33_quad)/u33_quad))
    end = time.clock()
    t_series.append(abs(t_quad/(end - start)))
u33_series = [float(x) for x in u33_series]

'''Step 6: 画图'''
from mpl_toolkits.mplot3d import Axes3D
fig = sk.plt.figure(figsize=(11,11))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(n_series, t_series, u33_series)
ax.scatter(n_series, t_series, zs=0, zdir='z',c='r', marker='o')
ax.scatter(n_series, u33_series, zs=max(t_series),zdir='y', c='b', marker='^')
ax.scatter(t_series, u33_series, zs=min(n_series),zdir='x', c='k', marker='d')

for i,j,k in zip(n_series,t_series,u33_series):
    ax.plot([i,i],[j,j],[min(u33_series),k],color = 'tan')
    #ax.plot([min(n_series),i],[j,j],[k,k],color = 'tan')
    #ax.plot([i,i],[j,max(t_series)],[k,k],color = 'tan')
    
ax.set_xlim(0.9*min(n_series), 1.1*max(n_series))
ax.set_ylim(0.9*min(t_series), 1.1*max(t_series))
ax.set_zlim(min(u33_series), max(u33_series))
ax.set_xlabel('Series number n')
ax.set_ylabel('Times of the time consume t_quad/t_series')
ax.set_zlabel('Relative error du/u')
ax.set_zscale('log')