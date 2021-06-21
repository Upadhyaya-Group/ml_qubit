
from time import ctime
import PythonCalculatorClient as calc


calcThread = calc.auto_connect();


# test the integration function of the calculator
calc.calculate("integrate(\"x+pi\",\"x\",0,1,0.001)");
calcworking = calc.calculate("ans == 3.64");
print(f"\ncalculator functioning?: {calcworking}");



times = [1,100,1000,100000];


# set variable values
variables = [
    ["p"     , 1        ], # stretched exponential
    ["ttwo"  , times[0] ], # coherence lifetime
    ["n"     , 10       ], # number of pi pulses
    ["tk"    , 10       ], # time that pi pulses are applies
    ["tpi"   , 10       ], # duration of pi pulses
    ["t"     , 10       ]  # time
]

# load variables into calculator
for i in range(0,len(variables)):
    calc.calculate(f"/{variables[i][0]} = {variables[i][1]}");


# integral calculator function
# (  pi/t2  )/(2*pi)*(  pi/t2  )*(    ( 1 + (-1)^(n+1)*exp(i*w*t)*cos(w*p/2) )^2 )/w^2
# https://www.integral-calculator.com/



'''
sw = "(  pi/ttwo  )"
summation_function = "(  (_1)^n+1  )";
fwt = f"(    ( 1 + (_1)^(n+1)*exp(i*w*t) + {summation_function}*exp(i*w*tk)*cos(w*tpi/2) )^2    )";
xt = f"integrate(\"{sw}/(2*pi)*{sw}*{fwt}/w^2\",\"w\",0.001,100,0.1)";
'''


xt = "integrate(\" (  pi/ttwo  )/(2*pi)*(  pi/ttwo  )*(    ( 1 + (_1)^(n+1)*exp(i*w*t)*cos(w*tpi/2) )^2 )/w^2\",\"w\",0.001,100000,0.001)";

print("\nSolving:");
print(xt);
print(" ")
print("approximation: " + calc.calculate(xt));


print("\n\ndone");
calcThread.join();
