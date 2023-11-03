
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
	static String[][][] map;
	static int x;
	static int y;
	static int z;
	static Queue<String> q = new LinkedList<String>();
	static int[][] movement = { { 1, 0, 0 }, { 0, 1, 0 }, { 0, 0, 1 }, { -1, 0, 0 }, { 0, -1, 0 }, { 0, 0, -1 } };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String data[] = br.readLine().split(" ");
		x = Integer.parseInt(data[0]);
		y = Integer.parseInt(data[1]);
		z = Integer.parseInt(data[2]);
		map = new String[x][y][z];
		for(int i=0;i<z;i++) {
			for(int j=0;j<y;j++) {
				data = br.readLine().split(" ");
				for(int k=0;k<x;k++) {
					map[k][j][i]=data[k];
					if(data[k].equals("1")) {
						q.add(k+","+j+","+i+","+"0");
					}
				}
			}
		}
		bfs();
	}
	
	static void bfs() {
		int result = 0;
		while(!q.isEmpty()) {
			String[] data = q.poll().split(",");
			int valX = Integer.parseInt(data[0]);
			int valY = Integer.parseInt(data[1]);
			int valZ = Integer.parseInt(data[2]);
			int cnt = Integer.parseInt(data[3]);
			for(int[] move:movement) {
				int nextX = valX+move[0];
				int nextY = valY+move[1];
				int nextZ = valZ+move[2];
				
				if(nextX>=0&&nextY>=0&&nextZ>=0&&nextX<x&&nextY<y&&nextZ<z) {
					if(map[nextX][nextY][nextZ].equals("0")) {
						q.add(nextX+","+nextY+","+nextZ+","+(cnt+1));
						map[nextX][nextY][nextZ]="-1";
						result=cnt;
					}
				}
			}
		}
		for(int i=0;i<z;i++) {
			for(int j=0;j<y;j++) {
				for(int k=0;k<x;k++) {
					if(map[k][j][i].equals("0")) {
						System.out.println("-1");
						return;
					}
				}
			}
		}
		System.out.println(result==0?0:result+1);
	}
}
