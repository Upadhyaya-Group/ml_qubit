import math
import numpy as np
from numpy.core.function_base import linspace
from scipy import integrate
from matplotlib import pyplot

ttwo = 343.43e-6;
p = 1;

def artificial_c(t): 
    return math.e**((-t/ttwo)**p);

def s(t): 
    return -math.pi*np.log(artificial_c(t))/t;

def filter_function(w,t, tpi=100e-9):
    t1 = (t + tpi)/2; 
    return ( abs( 1 + np.exp(1j*w*t) - 2*np.exp(1j*w*t1)*np.cos(w*tpi/2) ) )**2


# dx is the dx/dw
def dx(w, t):
    filter_function_vals = filter_function(w,t);
    return 0.5*math.pi * s(t) * filter_function_vals/ w**(2);


def x_quad(t):
    return integrate.quad(dx,0,math.inf,args=(t))[0];

def x_trapz(t):
    w = np.linspace(0.00001,1e7,10000);
    dx_vals = dx(w,t);
    return integrate.trapz(dx_vals, w);

def x(t):
    x_t_vals = np.array(t);
    for i in range(0,len(t)):
        x_t_vals[i] = (x_trapz(t[i]));
    return x_t_vals;

def c(t):
    return np.exp(-x(t));


def get_graphset(set_p=p,set_ttwo=ttwo):
    global p,ttwo;
    p = set_p;
    ttwo = set_ttwo;
    t_range = linspace(1e-6,5e-6,5000);
    return c(t_range), s(t_range);


if __name__ == "__main__":
    t_range = linspace(1e-6,5e-6,5000);
    c_t_vals = c(t_range);
    s_w_vals = s(t_range);

    
    
    figure, axis = pyplot.subplots(3, 2)


    # first graph set
    axis[0,0].set_title("c(t, p=1)");
    axis[0,0].plot(t_range,c_t_vals);
    
    axis[0,1].set_title("s(w, p=1)");
    axis[0,1].plot(math.pi/t_range,s_w_vals);


    # second graph set
    p = 2;

    c_t_vals = c(t_range);
    s_w_vals = s(t_range);
    
    axis[1,0].set_title("c(t, p=2)");
    axis[1,0].plot(t_range,c_t_vals);
    
    axis[1,1].set_title("s(w, p=2)");
    axis[1,1].plot(math.pi/t_range,s_w_vals);



    # third graph set
    p = 3;
    
    c_t_vals = c(t_range);
    s_w_vals = s(t_range);
    
    axis[2,0].set_title("c(t, p=3)");
    axis[2,0].plot(t_range,c_t_vals);
    
    axis[2,1].set_title("s(w, p=3)");
    axis[2,1].plot(math.pi/t_range,s_w_vals);


    pyplot.show();
