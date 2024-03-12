import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

public class Main {
	static int n;
	static int k;
	static Set<String> target;
	static int[] arr;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String data = br.readLine();
		
		n = Integer.parseInt(data);
		data = br.readLine();
		k = Integer.parseInt(data);
		
		arr = new int[n];
		target = new HashSet<>();
		
		for(int i =0; i< n; i++) {
			data = br.readLine();
			arr[i] = Integer.parseInt(data);
		}
//		System.out.println(Arrays.toString(arr));

		ArrayList<Integer> arr2= new ArrayList<>();
		
		dfs(0,"",arr2);
		System.out.println(target.size());
	}
	
	public static void dfs(int index, String val, ArrayList<Integer> saveArr) {
		
		if(index == k) {
			target.add(val);
			return;
		}
		
		for(int i =0; i < arr.length; i++) {
			if (!saveArr.contains(i)) {
				ArrayList<Integer> arr2= new ArrayList<>();
				for(int j=0;j<saveArr.size();j++){
					arr2.add(saveArr.get(j));
				}
				arr2.add(i);
				dfs(index+1,val+arr[i],arr2);
				
			}
		}
		
	}
}
