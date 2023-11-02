
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
	static int[] movement = new int[2];
	static boolean visit[];
	static int F;
	static int S;
	static int G;
	static int U;
	static int D;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] data = br.readLine().split(" ");
		F = Integer.parseInt(data[0]);
		S = Integer.parseInt(data[1]);
		G = Integer.parseInt(data[2]);
		U = Integer.parseInt(data[3]);
		D = Integer.parseInt(data[4]);
		movement[0] = U;
		movement[1] = -D;
		visit = new boolean[F];
		bfs();

	}

	static void bfs() {
		Queue<String> q = new LinkedList<String>();
		q.add((S-1)+","+"0");
		visit[S-1]=true;
		while (!q.isEmpty()) {
			String[] data = q.poll().split(",");
			int val =Integer.parseInt(data[0]);
			if(val==G-1) {
				System.out.println(Integer.parseInt(data[1]));
				return;
			}
			for(int move:movement) {
				int nextVal = move+val;
				if(nextVal<F&&nextVal>=0) {
					if(!visit[nextVal]) {
						visit[nextVal]=true;
						q.add(nextVal+","+(Integer.parseInt(data[1])+1));
					}
				}
			}
		}
		System.out.println("use the stairs");
	}
}
