
from numpy import exp, pi, cos, abs
from math import pow
import scipy.integrate as integrate
import matplotlib.pyplot as pyplot











times = [1/1000000];
ttwotimes = [100/1000];

p = 1;

tpi = 100/1000000000; # 100 ns

fx_vals = [];

def dx(w):
    global fx_vals;

    t = times[0];
    ttwo = ttwotimes[0];
    i = complex(0,1);

    filter_function = pow( abs(  1 + exp(i*w*t) - 2 * exp(i*w*(t+tpi)/2 ) * cos(w*tpi/2)  )  , 2);

    fx_vals.append(filter_function);

    dxt = 1/2/pi * pow(pi / ttwo,p) * pow( 1/w , p+1) * filter_function;

    return dxt;


xvals = range(1,30000000);
yvals = [];

for i in xvals:
    yvals.append(dx(i));


pyplot.plot(xvals,fx_vals);
pyplot.show();

