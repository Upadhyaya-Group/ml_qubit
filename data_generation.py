
from numpy import exp, pi, cos, abs
from math import pow
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





times = [1/1000000];
ttwotimes = [3.28/10000];

p = 1;

tpi = 100/1000000000; # 100 ns

# for plotting filter function
fx_vals = [];

def x(t):
    return integrate.quad(dx,0,30000,args=(t));


def dx(w,t):
    global fx_vals;

   # t = times[0];
    ttwo = ttwotimes[0];
    i = complex(0,1);

    filter_function = pow( abs(  1 + exp(i*w*t) - 2 * exp(i*w*(t+tpi)/2 ) * cos(w*tpi/2)  )  , 2);

    fx_vals.append(filter_function);

    dxt = 1/2/pi * pow(pi / ttwo,p) * pow( 1/w , p+1) * filter_function;

    return dxt;


plot(dx,1,300000,100,args=[times[0]]);
plot(x,0,1000,0.5);


