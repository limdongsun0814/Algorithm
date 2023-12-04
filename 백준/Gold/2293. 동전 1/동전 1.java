
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	static int n;
	static int k;
	static int[] val;
	static Integer[][] dp;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String data[]=br.readLine().split(" ");
		n = Integer.parseInt(data[0]);
		k = Integer.parseInt(data[1]);
		val = new int[n+1];
		val[0]=0;
		dp = new Integer[n+1][k+1];
		for(int i=0; i<k+1;i++) {
			dp[0][i]=0;
		}
		for(int i=0; i<n+1;i++) {
			dp[i][0]=1;
		}
		for(int i=0;i<n;i++) {
			val[i+1]=Integer.parseInt(br.readLine());
		}
		int result = method(n,k);
		System.out.println(result);
	}

	public static int method(int d,int v) {
		
		if(dp[d][v]!=null) {
			return dp[d][v];
		}
		if(val[d]>v){
			return method(d-1,v);
		}
		
		dp[d][v] = method(d-1,v)+method(d,v-val[d]);
		return dp[d][v];
	}
}
