package uniandes.algorithms.coinchange;

public class CoinChangeDynamic implements CoinChangeAlgorithm {

	@Override
	public int[] calculateOptimalChange(int totalValue, int[] denominations) {
		int[][] m = new int[denominations.length+1][totalValue+1];
		for (int i = 0; i <= denominations.length; i++) {
			for(int j = 0; j <= totalValue; j++) {
				if (j == 0) { m[i][j] = 0;}
				else if (i == 0 && j > 0) {m[i][j]= Integer.MAX_VALUE;}
				else if (denominations[i-1] > j) {m[i][j] = m[i-1][j];}
				else {m[i][j] = Math.min(1+m[i][j-denominations[i-1]], m[i-1][j]);}
			}
		}
		int[] res = new int[denominations.length];
		int i = denominations.length;
		int j = totalValue;
		while (i>0 && j >0) {
			if  (denominations[i-1]<=j && m[i][j] == m[i][j-denominations[i-1]]+1) {
				res[i]++;
				j-= denominations[i-1];
			}
			else if (denominations[i-1]>j && m[i][j] == m[i-1][j]) { 
				i--;
				}
		}
		return res;
	}

}
