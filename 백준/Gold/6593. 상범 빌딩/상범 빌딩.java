
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
	static char[][][] map;
	static int L;
	static int R;
	static int C;
	static String val;
	static String end;
	static int[][] movement = { { 1, 0, 0 }, { 0, 1, 0 }, { 0, 0, 1 }, { -1, 0, 0 }, { 0, -1, 0 }, { 0, 0, -1 } };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		while (true) {
			String data[] = br.readLine().split(" ");
			L = Integer.parseInt(data[0]);
			R = Integer.parseInt(data[1]);
			C = Integer.parseInt(data[2]);
			if(L==0 && R==0 && C==0) {
				break;
			}
			map = new char[L][R][C];
			for (int i = 0; i < L; i++) {
				for (int j = 0; j < R; j++) {
					char[] dataChar = br.readLine().toCharArray();
					for (int k = 0; k < C; k++) {
						map[i][j][k] = dataChar[k];
						if( dataChar[k]=='S') {
							val=i+","+j+","+k+","+"0";
						}else if(dataChar[k]=='E') {
							end=i+","+j+","+k+","+"0";
						}
					}
				}
				
				br.readLine();
			}
			bfs();
		}
		
	}

	static void bfs() {
		Queue<String> q = new LinkedList<String>();
		q.add(val);
		int x = Integer.parseInt(val.split(",")[0]);
		int y = Integer.parseInt(val.split(",")[1]);
		int z = Integer.parseInt(val.split(",")[2]);
		int xEnd = Integer.parseInt(end.split(",")[0]);
		int yEnd = Integer.parseInt(end.split(",")[1]);
		int zEnd = Integer.parseInt(end.split(",")[2]);
		map[x][y][z]='0';
		while(!q.isEmpty()){
			String valStr=q.poll();
			x = Integer.parseInt(valStr.split(",")[0]);
			y = Integer.parseInt(valStr.split(",")[1]);
			z = Integer.parseInt(valStr.split(",")[2]);
			int cnt = Integer.parseInt(valStr.split(",")[3]);
			if(x==xEnd&&y==yEnd&&z==zEnd) {
				System.out.println("Escaped in "+cnt+" minute(s).");
				return;
			}
			for(int[] move:movement) {
				int nextX = x+ move[0];
				int nextY = y+ move[1];
				int nextZ = z+ move[2];
				if(nextX==xEnd&&nextY==yEnd&&nextZ==zEnd) {
					System.out.println("Escaped in "+(cnt+1)+" minute(s).");
					return;
				}
				if(nextX>=0&&nextX<L&&nextY>=0&&nextY<R&&nextZ>=0&&nextZ<C) {
					if(map[nextX][nextY][nextZ]=='.') {
						q.add(nextX+","+nextY+","+nextZ+","+(cnt+1));
						map[nextX][nextY][nextZ]='0';
					}
				}
			}
		}
		System.out.println("Trapped!");
	}
}
