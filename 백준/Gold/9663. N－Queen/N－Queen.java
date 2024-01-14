

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;

public class Main {
	static int board[];
	static int N;
	static int cnt=0;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		board = new int[N];
		NQueen(0);
		System.out.println(cnt);
		
	}
	public static void NQueen(int new_index) {
		if(new_index==N) {
			cnt++;
			return;
		}
		for(int i=0;i<N;i++) {
			board[new_index]=i;
			if(ifCheck(new_index)){
				NQueen(new_index+1);
			}
		}
	}
	
	public static boolean ifCheck(int new_index) {
		for(int i=0;i<new_index;i++) {
			if(board[new_index]==board[i] || (new_index - i) == Math.abs(board[new_index]-board[i])) {
				return false;
			}
		}
		return true;
	}
}
