
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
	static int[][] map=new int[100][100];
	static boolean[][] visit=new boolean[100][100];
	static int map_size;
	static int max = 0;
	static int min = Integer.MAX_VALUE;
	static int result = 0;
	static int movement[][] = new int[][] {{1,2},{2,1},{2,-1},{1,-2},{-1,-2},{-2,-1},{-2,1},{-1,2}};

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int t=0;t<T;t++) {
			map_size=Integer.parseInt(br.readLine());
			map = new int[map_size][map_size];
			String data_arr[]=br.readLine().split(" ");
			String V = data_arr[0]+","+data_arr[1];
			data_arr=br.readLine().split(" ");
			String end_point = data_arr[0]+","+data_arr[1];
			String result=bfs(V,end_point);
			System.out.println(result.split(",")[2]);
		}
		
	}
	static String bfs(String V,String end_point) {
		Queue<String> q = new LinkedList<String>();
		int y = Integer.parseInt(V.split(",")[0]);
		int x = Integer.parseInt(V.split(",")[1]);
		int cnt=0;
		q.add(V+","+cnt);
		map[y][x] = 1;
		String val="0,0,0";
		int y_end = Integer.parseInt(end_point.split(",")[0]);
		int x_end = Integer.parseInt(end_point.split(",")[1]);
		while (!q.isEmpty()) {
			val = q.poll();
			y = Integer.parseInt(val.split(",")[0]);
			x = Integer.parseInt(val.split(",")[1]);
			cnt = Integer.parseInt(val.split(",")[2]);
			if(y==y_end && x==x_end) {
				break;
			}
			for(int[] move:movement) {
				int next_val_y = y+move[0];
				int next_val_x = x+move[1];
				if(next_val_y<map_size&&next_val_x<map_size&&next_val_y>=0&&next_val_x>=0) {
					if(map[next_val_y][next_val_x]!=1) {
						map[next_val_y][next_val_x]=1;
						q.add(next_val_y+","+next_val_x+","+(cnt+1));
					}
				}
			}
		}
		return val;
	}
}
