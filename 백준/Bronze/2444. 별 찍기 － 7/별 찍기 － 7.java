import java.util.Scanner;
import java.io.FileNotFoundException;
public class Main {
	
	public static void main(String[] args) throws FileNotFoundException {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		StringBuffer str = new StringBuffer();
		StringBuffer str2 = new StringBuffer();
		for(int i=0;i<n-1;i++) {
			str2.append(" ");
		}
		for(int i = 0; i<n;i++) {
			str.append("*");
			System.out.println(str2.substring(0,n-i-1)+str.toString()+str.substring(0,i));
		}
		for(int i = 0; i<n-1;i++) {
			System.out.println(str2.substring(0,i+1)+str.substring(0,n-(i+1))+str.substring(0,n-(i+1)-1));
		}
	}
}