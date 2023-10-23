import java.util.Scanner;
import java.io.FileNotFoundException;
public class Main {
	
	public static void main(String[] args) throws FileNotFoundException {
		Scanner sc = new Scanner(System.in);
		while(sc.hasNextLine()) {
			String data_int = sc.nextLine();
			System.out.println(data_int);
		}
	}
}