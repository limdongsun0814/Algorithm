import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T =Integer.parseInt(br.readLine());
		Set<String> set = new HashSet<String>();
		int cnt=0;
		for(int tt=0;tt<T;tt++) {
			String str_data = br.readLine();
			if(str_data.equals("ENTER")) {
				cnt+=set.size();
				set = new HashSet<String>();
			}else{
				set.add(str_data);
			}
		}
		cnt+=set.size();
		System.out.println(cnt);
	}
}