import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.CharBuffer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.ListIterator;
import java.util.LinkedList;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String data = br.readLine();
		Character[] arr_char=CharBuffer.wrap(data.toCharArray())
					.chars()
					.mapToObj(c->(char) c)
					.toArray(Character[]::new);
		LinkedList<Character> arr = new LinkedList<Character>(Arrays.asList(arr_char));
		
		
		ListIterator<Character> lsit = arr.listIterator(arr.size());
		
//		for(char chr: data.toCharArray()) {
//			lsit.add(chr);
//		}
			
		
		int T = Integer.parseInt(br.readLine());
		for (int ii = 0; ii < T; ii++) {
			String[] 연산 = br.readLine().split(" ");
			switch (연산[0]) {
			case "P":
//				for(char chr: 연산[1].toCharArray()) {
					lsit.add(연산[1].charAt(0));
//				}
				break;
			case "L":
				if(lsit.hasPrevious()) {
				lsit.previous();
				}
				break;
			case "D":
				if(lsit.hasNext()) {
				lsit.next();
				}
				break;
			case "B":
				if(lsit.hasPrevious()) {
				lsit.previous();
				lsit.remove();
				}
				break;
			}

		}
		String str = arr.toString();
		str=str.replaceAll(" ", "");
		str=str.replaceAll(",", "");
		System.out.println(str.substring(1,str.length()-1));
//		for(String strp:arr) {
//			System.out.print(strp);
//		}
	}
	
}