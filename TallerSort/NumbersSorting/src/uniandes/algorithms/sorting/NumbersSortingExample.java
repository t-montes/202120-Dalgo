package uniandes.algorithms.sorting;
import java.io.BufferedReader;
import java.io.FileReader;
import java.lang.reflect.Constructor;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class NumbersSortingExample {

	/**
	 * Main method for the numbers sorter example. It requires three parameters:
	 * args[0]: Input file with numbers to sort. It must be a text file with one number per line
	 * args[1]: (Optional) Algorithm used to sort the numbers. It can be Bubble, Merge or Quick.
	 * If not provided, the default algorithm implemented in the static method sort of the class
	 * java.util.Arrays is used
	 * @param args Array with the arguments described above 
	 * @throws Exception if the input file does not exist or it can not be read
	 * @throws Exception If the algorithm is not implmented
	 */
	public static void main(String[] args) throws Exception {
		//Read parameters
		String inFilename = args[0];
		String algorithm = null;
		if(args.length>1) algorithm = args[1];
		
		//Read input file
		List<Integer> numbersList = new ArrayList<>();
		
		
		try (FileReader reader = new FileReader(inFilename);
			 BufferedReader in = new BufferedReader(reader)) { 
			String line = in.readLine();
			for (int i=0;line != null;i++) {
				try {
					numbersList.add(Integer.parseInt(line));
				} catch (Exception e) {
					System.err.println("Can not read number from line "+i+" content: "+line);
					e.printStackTrace();
				}
				line = in.readLine();
			}
		}
		int [] numbers = new int [numbersList.size()];
		for(int i=0;i<numbers.length;i++) numbers[i] = numbersList.get(i);
		
		//Sort values
		long startTime;
		long endTime;
		if(algorithm==null) {
			startTime = System.currentTimeMillis();
			Arrays.sort(numbers);
			endTime = System.currentTimeMillis();
		} else {
			String classname = NumbersArraySorter.class.getPackage().getName()+"."+algorithm+"NumbersArraySorter";
			NumbersArraySorter sortAlgorithm;
			try {
				Class<?> algorithmClass = Class.forName(classname);
				Constructor<?> emptyConstructor = algorithmClass.getConstructor();
				sortAlgorithm = (NumbersArraySorter)emptyConstructor.newInstance();
			} catch (Exception e) {
				throw new Exception("Invalid algorithm "+algorithm,e);
			}
			startTime = System.currentTimeMillis();
			sortAlgorithm.sort(numbers);
			endTime = System.currentTimeMillis();
		}
		
		//Output answer
		for(int i=0;i<numbers.length;i++) {
			if(i>0 && (numbers[i]<numbers[i-1])) throw new RuntimeException("ERROR: Disorder detected at position "+i+" values: "+numbers[i-1]+","+numbers[i]);
			System.out.println(numbers[i]);
		}
		System.err.println("Numbers sorted. Total time(milliseconds): "+(endTime-startTime));
	}

}
