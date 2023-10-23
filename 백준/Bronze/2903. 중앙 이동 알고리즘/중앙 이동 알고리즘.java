
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;

public class Main {


	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int a= 3;
		for(int i=1;i<n;i++) {
			a=a+a-1;
		}
		System.out.println(a*a);
	}
}
