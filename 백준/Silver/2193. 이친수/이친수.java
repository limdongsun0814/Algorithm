
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;

public class Main {
	static long[] dp;
	static int n;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		dp = new long[n + 1];
		long result = fibo(n);
		System.out.println(result);
	}

	public static long fibo(int x) {
		if (x == 1) {
			return 1;
		}
		if (x == 2) {
			return 1;
		}
		if (dp[x] != 0) {
			return dp[x];
		}
		dp[x] = fibo(x - 1) + fibo(x - 2);
		return dp[x];
	}
}