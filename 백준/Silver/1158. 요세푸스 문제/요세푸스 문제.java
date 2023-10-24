
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;
import java.util.stream.IntStream;


public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str_arr = br.readLine().split(" ");
		int N=Integer.parseInt(str_arr[0]);
		int K=Integer.parseInt(str_arr[1]);
		
		Integer[] arr = IntStream.range(1, N+1).mapToObj(i->(int) i).toArray(Integer[]::new);
		Queue<Integer> q = new LinkedList<Integer>(Arrays.asList(arr));
		ArrayList<Integer> arr_list = new ArrayList<Integer>();
		while(arr_list.size()<N) {
			for(int i=0; i<K-1; i++) {
				q.offer(q.poll());
			}
			Integer number = q.poll();
			if(number!=null)
			arr_list.add(number);
		}
		String result = arr_list.toString();
		result = result.replace("[", "<");
		result = result.replace("]", ">");
		System.out.println(result);
	}
}
