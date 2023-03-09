package uniandes.algorithms.coinchange;

public class CoinChangeRecursive implements CoinChangeAlgorithm{
	@Override
	public int[] calculateOptimalChange(int totalValue, int[] denominations) {
		int[] m = new int[denominations.length];
		int[] res = implementRecursion(m, totalValue, denominations, denominations.length+1);
		return res;
	}
	
	public int[] implementRecursion(int[] answer, int totalValue, int[] denominations, int i) {
		if(i == 0 && totalValue > 0 ) {
			return answer;
		}
		else if (totalValue < 0) {
			return answer;
		}
		else if (totalValue == 0) {
			return answer;
		}
		else{
			int[] includeArray = answer.clone();
			int[] excludeArray = answer.clone();
			includeArray[i-1] += 1;
			int[] include = implementRecursion(includeArray, totalValue - denominations[i-1], denominations, i);
			int[] exclude = implementRecursion(excludeArray, totalValue, denominations, i-1);
			int sumInclude = getSumArray(include);
			int sumExclude = getSumArray(exclude);
			if (sumInclude < sumExclude) {return include;}
			else {return exclude;}
		}
	}
	
	private int getSumArray(int[] array) {
		int sum = 0;
		for(int a: array) {
			sum+= a;
		}
		return sum;
	}
}
