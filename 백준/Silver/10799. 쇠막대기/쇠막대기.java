
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		char[] data = br.readLine().toCharArray();
		int start = 0;
		int end = 0;
		int 레이저가_막대기를_관통한_수 = 0;
		int flog = 0;
		int 막대기_갯수=0;
		for (int index = 0; index < data.length - 1; index++) {
			if (data[index] == '(') {
				start++;
			} else {
				end++;
			}
			if ((data[index] + "" + data[index + 1]).equals("()")) {
				if (start > 1) {
					end++;
					레이저가_막대기를_관통한_수 += start - end;
					end--;
				}
			}
			if(!(data[index] + "" + data[index + 1]).equals("()")&&data[index] == '(') {
				막대기_갯수++;
			}
		}
		System.out.println(레이저가_막대기를_관통한_수+막대기_갯수);
	}
}