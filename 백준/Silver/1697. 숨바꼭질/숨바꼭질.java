import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
	static HashMap<Integer, Boolean> visit =  new HashMap<Integer, Boolean>();
	static int[] movement = new int[3];
	static int N;
	static int M;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] data = br.readLine().split(" ");
		N=Integer.parseInt(data[0]);
		M=Integer.parseInt(data[1]);
		movement[0]=1;
		movement[1]=-1;
		bfs();
	}

	static void bfs() {
		Queue<String> q = new LinkedList<String>();
		q.add(N+","+0);
		visit.put(N, true);
		while(!q.isEmpty()) {
			String[] data=q.poll().split(",");
			int val =Integer.parseInt(data[0]);
			int cnt =Integer.parseInt(data[1]);
			movement[2]=val;
			if(val==M) {
				System.out.println(cnt);
				break;
			}
			for(int move:movement) {
				int nextVal = move+val;
				if(nextVal>=0&&nextVal<200001) {
					if(visit.get(nextVal)==null) {
						q.add(nextVal+","+(cnt+1));
						visit.put(nextVal, true);
					}
				}
			}
		}
	}
}
