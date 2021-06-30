
from numpy import exp, pi, cos, abs
from math import inf, pow
import scipy.integrate as integrate
import matplotlib.pyplot as pyplot





def plot(fx,lowerBound=0, upperBound=1000, step=1, args=[]):

    i = lowerBound;

    xvals = [];
    yvals = [];

    Y = 0;

    while(i < upperBound):
        xvals.append(i);
        if (len(args) > 0):
            if (len(args) == 1): 
                    y = fx(i*step,args[0]); 

                    yvals.append(y);           
            else:
                    y = fx(i*step,args);
                    yvals.append(y); 
                    
        else:
            y = fx(i*step);
            yvals.append(y); 

        i += step;

    pyplot.plot(xvals,yvals);
    pyplot.show();





times = [1E-6];
ttwotimes = [3.28/10000];

p = 1; 

tpi = 100E-9; # 100 ns


# for plotting filter function
fx_vals = [];


def dx(w,t):
    global fx_vals;

    ttwo = ttwotimes[0];


    filter_function = pow( abs(  1 + exp(1j*w*t) - 2 * exp(1j*w*(t+tpi)/2 ) * cos(w*tpi/2)  )  , 2);


    dxt = 1/2/pi * pow(pi / ttwo,p) * pow( 1/w , p+1) * filter_function;

    return dxt;


def x(t):
    return integrate.quad(dx,0,inf,args=(t))[0];


def c(t):
    return exp(-x(t));


plot(dx,1,300000,100,args=[times[0]]);
plot(x,0,1000,0.5);


