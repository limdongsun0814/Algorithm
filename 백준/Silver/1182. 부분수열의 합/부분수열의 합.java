
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	static int board[];
	static int arr[];
	static int N;
	static int S;
	static int cnt=0;
	static int count=0;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String data[] = br.readLine().split(" ");
		N = Integer.parseInt(data[0]);
		S = Integer.parseInt(data[1]);
		board = new int[N];
		arr = new int[N];
		data = br.readLine().split(" ");
		for(int i=0;i<N;i++) {
			arr[i]=Integer.parseInt(data[i]);
		}
//		System.out.println(Arrays.toString(arr));
		subsequence(-1, 0,false);
		System.out.println(cnt);
//		System.out.println(S);
	}
	public static void subsequence(int new_index,int value,boolean flag) {
		if(value==S&&flag) {
//			System.out.println(value+"aa"+new_index);
			cnt++;
		}
		for(int i=new_index+1;i<N;i++) {
			subsequence(i,value+arr[i],true);
		}
		
	}
	

}