package data_generation;

import calculatorv2_core.Equation;
import calculatorv2_core.Equation.DegOrRadValue;

public abstract class Data_generation {
	
	public static void main(String[] args) {
		
		Equation eq = new Equation();
		eq.setDegRadMode(DegOrRadValue.radians);
		eq.importAll();
		eq.importStandardConstants();
		
		eq.calculate("/eq = \"square( abs(  1 + exp(i*w*t) - 2 * exp(i*w*(t+tpi)/2 ) * cos(w*tpi/2)  ) )\"");
		
		eq.calculate("/tpi = 100E_9");
		eq.calculate("/w = 100");
		eq.calculate("/t = 1E_6");

		eq.calculate("graph(eq,\"w\",0,6E7,16)");


		eq.calculate("graph(eq,\"w\",0,6E6,1E_8)");

		eq.calculate("graph('integrate(eq,\"w\",0,3000,0.1)',\"t\")");
		

		
	
	}
}
