
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt( br.readLine());
		for(int iiiiiii=0;iiiiiii<T;iiiiiii++) {
			int size = Integer.parseInt( br.readLine());
			PriorityQueue<Integer> minValue = new PriorityQueue<>();
			PriorityQueue<Integer> maxValue = new PriorityQueue<>((o1, o2) -> o2-o1);
			String[] data = br.readLine().split(" ");
			
			for(String i: data) {
				minValue.add(Integer.parseInt(i));
				maxValue.add(Integer.parseInt(i));
			}
			System.out.println(minValue.poll()+" "+maxValue.poll());
		}
	}
}
