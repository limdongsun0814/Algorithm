
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Arrays;


public class Main {
	static int number_arr[];
	static int Operator_cnt[];
	static int using_cnt[];
	static int N;
	static int cnt=0;
	static int min=Integer.MAX_VALUE;
	static int max=Integer.MIN_VALUE;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		number_arr = new int[N];
		Operator_cnt = new int[4];
		using_cnt = new int[N-1];
		
		String[] data=br.readLine().split(" ");
		for(int i=0;i<N;i++) {
			number_arr[i]=Integer.parseInt(data[i]);
		}
		
		for(int i=0;i<N-1;i++) {
			using_cnt[i]=0;
		}
		data=br.readLine().split(" ");
		for(int i=0; i<4;i++) {
			Operator_cnt[i]=Integer.parseInt(data[i]);
		}
		Operator(0,number_arr[0],5);
		System.out.println(max);
		System.out.println(min);
	}
	public static void Operator(int new_index,int value,int status) {
		if(status!=5) {
			using_cnt[new_index-1]=status;
		}
		
		if(new_index+1==N) {
			max=max<value?value:max;
			min=min>value?value:min;
			return;
		}
		
		int[] cnt = new int[4];
		for(int i=0;i<new_index;i++) {
			cnt[using_cnt[i]]++;
		}
		
		if(cnt[0]<Operator_cnt[0]) {
			Operator(new_index+1,value+number_arr[new_index+1],0);
		}
		if(cnt[1]<Operator_cnt[1]) {
			Operator(new_index+1,value-number_arr[new_index+1],1);
		}
		if(cnt[2]<Operator_cnt[2]) {
			Operator(new_index+1,value*number_arr[new_index+1],2);
		}
		if(cnt[3]<Operator_cnt[3]) {
			Operator(new_index+1,value/number_arr[new_index+1],3);
		}
	}
}
