# Velocity funcitons
# Every funciton has the claim r = np.sqrt(x**2 + y**2). It must need simplify such as decorator.

def v11_larger_h(x, y, z, h, H, imax=4.0):
    r = np.sqrt(x**2 + y**2)
    return  np.array(integrate.quad(j0sh, 0, imax,args=(r, z, h, H))) + \
            x**2 / r * h0 *  np.array(integrate.quad(j1xsh, 0, imax,args=(r, z, h, H)))

def v11_smaller_h(x, y, z, h, H, imax=4.0):
    r = np.sqrt(x**2 + y**2)
    return  np.array(integrate.quad(j0sh, 0, imax,args=(r, H-z, H-h, H))) + \
            x**2 / r * h0 *  np.array(integrate.quad(j1xsh, 0, imax,args=(r, H-z, H-h, H)))

def v11(x, y, z, h, H, imax=4.0):
    (z, h) = (z, h) if z > h else (H - z, H - h)
    r = np.sqrt(x**2 + y**2)
    return  np.array(integrate.quad(j0sh, 0, imax,args=(r, z, h, H))) + \
            x**2 / r * h0 * np.array(integrate.quad(j1xsh, 0, imax,args=(r, z, h, H)))

def w11(x, y, z, h, H, imax=4.0):
    r = np.sqrt(x**2 + y**2)
    return (x**2 - y**2) / (r**3 * np.sqrt(h0)) * np.array(integrate.quad(j1xa1, 0, imax, args=(r, z, h, H))) - \
            x**2 / r**2 * np.array(integrate.quad(j0x2a1, 0, imax, args=(r, z, h, H)))

# ===================================================
def v12_larger_h(x, y, z, h, H, imax=4.0):
    r = np.sqrt(x**2 + y**2)
    return  x * y / r * h0 * np.array(integrate.quad(j1xsh, 0, imax,args=(r, z, h, H)))

def v12_smaller_h(x, y, z, h, H, imax=4.0):
    r = np.sqrt(x**2 + y**2)
    return  x * y / r * h0 * np.array(integrate.quad(j0sh, 0, imax,args=(r, H-z, H-h, H)))

def v12(x, y, z, h, H, imax=4.0):
    (z, h) = (z, h) if z > h else (H - z, H - h)
    r = np.sqrt(x**2 + y**2)
    return  x * y / r * h0 * np.array(integrate.quad(j1xsh, 0, imax,args=(r, z, h, H)))

def w12(x, y, z, h, H, imax=4.0):
    r = np.sqrt(x**2 + y**2)
    return (2*x*y) / (r**3 * np.sqrt(h0)) * np.array(integrate.quad(j1xa1, 0, imax, args=(r, z, h, H))) - \
            x * y / r**2 * np.array(integrate.quad(j0x2a1, 0, imax, args=(r, z, h, H)))

# =====================================================
def v13_larger_h(x, y, z, h, H, imax=4.0):
    r = np.sqrt(x**2 + y**2)
    return (z - h) * x / r * h0 *  np.array(integrate.quad(j1xsh, 0, imax,args=(r, z, h, H)))

def v13_smaller_h(x, y, z, h, H, imax=4.0):
    r = np.sqrt(x**2 + y**2)
    return  (z - h) * x / r * h0 *  np.array(integrate.quad(j1xsh, 0, imax,args=(r, H-z, H-h, H)))

def v13(x, y, z, h, H, imax=4.0):
    (z1, h1) = (z, h) if z > h else (H - z, H - h)
    r = np.sqrt(x**2 + y**2)
    return (z - h) * x / r * h0 *  np.array(integrate.quad(j1xsh, 0, imax,args=(r, z1, h1, H)))

def w13(x, y, z, h, H, imax=4.0):
    r = np.sqrt(x**2 + y**2)
    return x / r * np.array(integrate.quad(j1xa4_13, 0, imax, args=(r, z, h, H)))

# =====================================================   
def v31_larger_h(x, y, z, h, H, imax=4.0):
    r = np.sqrt(x**2 + y**2)
    return (z - h) * x / r * h0 *  np.array(integrate.quad(j1xsh, 0, imax,args=(r, z, h, H)))

def v31_smaller_h(x, y, z, h, H, imax=4.0):
    r = np.sqrt(x**2 + y**2)
    return  (z - h) * x / r * h0 *  np.array(integrate.quad(j1xsh, 0, imax,args=(r, H-z, H-h, H)))

def v31(x, y, z, h, H, imax=4.0):
    (z1, h1) = (z, h) if z > h else (H - z, H - h)
    r = np.sqrt(x**2 + y**2)
    return (z - h) * x / r * h0 *  np.array(integrate.quad(j1xsh, 0, imax,args=(r, z1, h1, H)))

def w31(x, y, z, h, H, imax=4.0):
    r = np.sqrt(x**2 + y**2)
    return x / r * np.array(integrate.quad(j1xa4_31, 0, imax, args=(r, z, h, H)))

# =====================================================
def v33_larger_h(x, y, z, h, H, imax=4.0):
    r = np.sqrt(x**2 + y**2)
    return np.array(integrate.quad(j0sh, 0, imax,args=(r, z, h, H))) + \
            x**2 / r * h0 *  np.array(integrate.quad(j0xdsh, 0, imax,args=(r, z, h, H)))

def v33_smaller_h(x, y, z, h, H, imax=4.0):
    r = np.sqrt(x**2 + y**2)
    return np.array(integrate.quad(j0sh, 0, imax,args=(r, H-z, H-h, H))) - \
            np.array(integrate.quad(j0xdsh, 0, imax,args=(r, H-z, H-h, H)))

def v33(x, y, z, h, H, imax=4.0):
    (z, h) = (z, h) if z > h else (H - z, H - h)
    r = np.sqrt(x**2 + y**2)
    return np.array(integrate.quad(j0sh, 0, imax,args=(r, z, h, H))) + \
            x**2 / r * h0 *  np.array(integrate.quad(j0xdsh, 0, imax,args=(r, z, h, H)))
    
def w33(x, y, z, h, H, imax=4.0):
    r = np.sqrt(x**2 + y**2)
    return np.array(integrate.quad(j0a2, 0, imax, args=(r, z, h, H)))

    
# u11 ========================================= 

def v11(x, y, z, h, H, imax=4.0):
    (z, h) = (z, h) if z > h else (H - z, H - h)
    r = np.sqrt(x**2 + y**2)
    if z > h + 1/ mp.e:
        return  (far_integral(j0sh, r, z, h, H, imax, method='gauss-legendre') + 
                x**2 / r * h0 * far_integral(j1xsh, r, z, h, H, imax, method='gauss-legendre'))
    else:
        return  (near_integral(j0sh, r, z, h, H, m=0) + 
                x**2 / r * h0 * near_integral(j1xsh, r, z, h, H, m=1))

def w11(x, y, z, h, H, imax=4.0):
    r = np.sqrt(x**2 + y**2)
    return ((x**2 - y**2) / (r**3 * np.sqrt(h0)) * far_integral(j1xa1, r, z, h, H, imax, method='gauss-legendre') - 
            x**2 / r**2 * far_integral(j0x2a1, r, z, h, H, imax, method='gauss-legendre'))

# u12 =========================================

def v12(x, y, z, h, H, imax=4.0):
    (z, h) = (z, h) if z > h else (H - z, H - h)
    r = np.sqrt(x**2 + y**2)
    if z > h + 1/ mp.e:
        return x * y / r * h0 * far_integral(j1xsh, r, z, h, H, imax, method='gauss-legendre')
    else:
        return x * y / r * h0 * near_integral(j1xsh, r, z, h, H, m=1)

def w12(x, y, z, h, H, imax=4.0):
    r = np.sqrt(x**2 + y**2)
    return ((2*x*y) / (r**3 * np.sqrt(h0)) * far_integral(j1xa1, r, z, h, H, imax, method='gauss-legendre') - 
            x * y / r**2 * far_integral(j0x2a1, r, z, h, H, imax, method='gauss-legendre'))

# u13 =========================================

# =====================================================
# The piecewise function of v13 needs further consideration.
# z = h may never hold for the float presicion.
def v13(x, y, z, h, H, imax=4.0):
    (z, h) = (z, h) if z > h else (H - z, H - h)
    r = np.sqrt(x**2 + y**2)
    if z > h:
        return (z - h) * x / r * h0 * far_integral(j1xsh, r, z, h, H, imax, method='gauss-legendre')
    else:
        return 0

def w13(x, y, z, h, H, imax=4.0):
    r = np.sqrt(x**2 + y**2)
    return x / r * far_integral(j1xa4_13, r, z, h, H, imax, method='gauss-legendre')

# u31 =========================================

def v31(x, y, z, h, H, imax=4.0):
    return v13(x, y, z, h, H, imax=4.0)

def w31(x, y, z, h, H, imax=4.0):
    r = np.sqrt(x**2 + y**2)
    return x / r * far_integral(j1xa4_31, r, z, h, H, imax, method='gauss-legendre')

# u33 =========================================

def v33(x, y, z, h, H, imax=4.0):
    (z, h) = (z, h) if z > h else (H - z, H - h)
    r = np.sqrt(x**2 + y**2)
    if z > h + 1/ mp.e: 
        return (far_integral(j0sh, r, z, h, H, imax, method='gauss-legendre') + 
                x**2 / r * h0 *  far_integral(j0xdsh, r, z, h, H, imax, method='gauss-legendre')
    else:
        return (near_integral(j0sh, r, z, h, H, imax, method='gauss-legendre') + 
                x**2 / r * h0 *  far_integral(j0xdsh, r, z, h, H, imax, method='gauss-legendre')
    
    
def w33(x, y, z, h, H, imax=4.0):
    r = np.sqrt(x**2 + y**2)
    return far_integral(j0a2, r, z, h, H, imax, method='gauss-legendre')


# 将速度函数包装为矢量函数。
# U11 =========================================

def U11_z(x, y, z_list, h, H, imax=4.0):
    if (type(x) or type(y)) is not float:
        raise TypeError("x and y should be float!")
    elif type(z_list) is not np.ndarray:
        raise TypeError("z should be array!")
    global r    
    r = np.sqrt(x**2 + y**2)
    return np.array([w11(x, y, zz, h, H, imax) + v11(x, y, zz, h, H, imax) 
                    for zz in z_list])

# U12 =========================================

def U12_z(x, y, z_list, h, H, imax=4.0):
    if (type(x) or type(y)) is not float:
        raise TypeError("x and y should be float!")
    elif type(z_list) is not np.ndarray:
        raise TypeError("z should be array!")
    global r    
    r = np.sqrt(x**2 + y**2)
    return np.array([w12(x, y, zz, h, H, imax) + v12(x, y, zz, h, H, imax) 
                    for zz in z_list])

# U13 =========================================

def U13_z(x, y, z_list, h, H, imax=4.0):
    if (type(x) or type(y)) is not float:
        raise TypeError("x and y should be float!")
    elif type(z_list) is not np.ndarray:
        raise TypeError("z should be array!")
    global r    
    r = np.sqrt(x**2 + y**2)
    return np.array([w13(x, y, zz, h, H, imax) + v13(x, y, zz, h, H, imax) 
                    for zz in z_list])

# U31 =========================================

def U31_z(x, y, z_list, h, H, imax=4.0):
    if (type(x) or type(y)) is not float:
        raise TypeError("x and y should be float!")
    elif type(z_list) is not np.ndarray:
        raise TypeError("z should be array!")
    global r    
    r = np.sqrt(x**2 + y**2)
    return np.array([w31(x, y, zz, h, H, imax) + v31(x, y, zz, h, H, imax) 
                    for zz in z_list])