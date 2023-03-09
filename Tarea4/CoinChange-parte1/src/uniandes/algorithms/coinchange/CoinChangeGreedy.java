package uniandes.algorithms.coinchange;

import java.util.Arrays;

public class CoinChangeGreedy implements CoinChangeAlgorithm{

	@Override
	public int[] calculateOptimalChange(int totalValue, int[] denominations) {
		Arrays.sort(denominations);
		int[] ans = new int[denominations.length];
		int i = denominations.length -1;
		while (i >= 0) {
			while(totalValue >= denominations[i]) {
				totalValue -= denominations[i];
				ans[i]++;		
			}
			i--;
		}
		return ans;
	}

}
