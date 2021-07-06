package data_generation;

import calculatorv2_core.Equation;

public abstract class Data_generation {
	
	public static void main(String[] args) {
		
		Equation eq = new Equation();
		eq.importAll();
		
		String output = eq.calculate("run(\"ml_qubit.cobra\")");
		
		System.out.println(output);
		
	
	}
}
