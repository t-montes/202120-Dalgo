package uniandes.algorithms.sorting;

/**
 * Implements the merge sort algorithm for number arrays
 */
public class MergeNumbersArraySorter implements NumbersArraySorter {

	/**
	 * Method extracted from ISIS1105 class slides, and modified to fit the example.
	 */
	private void mergeSort(int[] numbers, int first, int last) {
		if (first==last) return;
		int m = (first+last)/2;
		mergeSort(numbers, first, m);
		mergeSort(numbers, m+1, last);
		
		//merge sorted lists
		
		int [] mergedSet = new int[numbers.length];
		int i=first;
		int j=m+1;
		int index = 0;
		while(i<=m && j <=last) {
			int n1 = numbers[i];
			int n2 = numbers[j];
			
			if (n1 < n2) {
				mergedSet[index] = n1;
				i++;
			} else {
				mergedSet[index] = n2;
				j++;
			}
			index++;
		}
		
		for (;i<=m;i++,index++) mergedSet[index] = numbers[i];
		for (;j<=last;j++,index++) mergedSet[index] = numbers[j];
		
		for (int k=0;k<mergedSet.length;k++) {
			numbers[first+k] = 
					mergedSet[k];
		}
		
	}
	
	@Override
	/**
	 * @author: Tony Santiago Montes Buitrago
	 */
	public void sort(int [] numbers) {
		mergeSort(numbers, 0, numbers.length-1);
	}

}
