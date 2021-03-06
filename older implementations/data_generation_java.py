

import PythonCalculatorClient as calc

calcThread = calc.auto_connect();


# test the integration function of the calculator
calc.calculate("integrate(\"x+pi\",\"x\",0,1,0.001)");
calcworking = calc.calculate("ans == 3.64");
print(f"\ncalculator functioning?: {calcworking}");

p = 1;

# set variable values
variables = [
    ["p"     , p            ], # stretched exponential
    ["ttwo"  , ttwotimes[0] ], # coherence lifetime
    ["n"     , 10           ], # number of pi pulses
    ["tk"    , 10           ], # time that pi pulses are applies
    ["tpi"   , 100          ], # duration of pi pulses (ns)
    ["t"     , times[0]     ]  # time
]

# load variables into calculator
for i in range(0,len(variables)):
    calc.calculate(f"/{variables[i][0]} = {variables[i][1]}");

xt = "integrate(\" (  pi/ttwo  )/(2*pi)*(  pi/ttwo  )*(    ( 1 + (_1)^(n+1)*exp(i*w*t)*cos(w*tpi/2) )^2 )/w^2\",\"w\",0.001,100000,0.001)";

print("\nSolving:");
print(xt);
print(" ")
print("approximation: " + calc.calculate(xt));


print("\n\ndone");
calcThread.join();