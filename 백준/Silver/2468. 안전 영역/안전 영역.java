import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
	static int[][] map=new int[100][100];
	static boolean[][] visit=new boolean[100][100];
	static int N;
	static int max = 0;
	static int min = Integer.MAX_VALUE;
	static int result = 1;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String data = br.readLine();
		N = Integer.parseInt(data);
		visit = new boolean[N][N];
		map = new int[N][N];
		HashSet<Integer> h_set = new HashSet<Integer>();
		
		for (int i = 0; i < N; i++) {
			String[] str_arr = br.readLine().split(" ");
			for (int j = 0; j < N; j++) {
				map[i][j] = Integer.parseInt(str_arr[j]);
				max = max < map[i][j] ? map[i][j] : max;
				min = min > map[i][j] ? map[i][j] : min;
				h_set.add(map[i][j]);
			}
		}
		for (int h:h_set) {
			int cnt = 0;
			visit_reset(h);
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (!visit[i][j]) {
						dfs(i,j);
						cnt++;
					}
				}
			}
			result = result < cnt ? cnt : result;
		}
		System.out.println(result);
	}
	static void visit_reset(int h) {
		for(int i=0; i<N;i++) {
			for(int j=0; j<N; j++) {
				visit[i][j] = map[i][j] >= h ? false : true;
			}
		}
	}
	static String find_v(int h) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (!visit[i][j])
					return i + "," + j;
			}
		}
		return "end";
	}

	static void dfs(int y,int x) {
		visit[y][x]=true;
		
		if (y + 1 < N) {
			if ( !visit[y + 1][x] ) {
				visit[y+1][x] = true;
				dfs(y+1,x);
			}
		}

		if (x + 1 < N) {
			if ( !visit[y][x + 1]) {
				visit[y][x+1] = true;
				dfs(y,x+1);
			}
		}
		
		if (y - 1 >= 0) {
			if (!visit[y - 1][x]) {
				visit[y-1][x] = true;
				dfs(y-1,x);
			}
		}

		if (x - 1 >= 0) {
			if ( !visit[y][x - 1]) {
				visit[y][x-1] = true;
				dfs(y,x-1);
			}
		}
	}
}
