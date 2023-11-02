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
	static char[][] map;
	static int w;
	static int h;
	static int[][] movement = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int ii = 0; ii < T; ii++) {
			String[] wh = br.readLine().split(" ");
			w = Integer.parseInt(wh[0]);
			h = Integer.parseInt(wh[1]);
			map = new char[h][w];
			for (int i = 0; i < h; i++) {
				char[] arr = br.readLine().toCharArray();
				for (int j = 0; j < w; j++) {
					map[i][j] = arr[j];
				}
			}
			bfs();
		}
	}

	static void bfs() {
		Queue<String> qF = new LinkedList<String>();
		Queue<String> qP = new LinkedList<String>();
		int cntF = 0;
		int cntP = 0;
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				if (map[i][j] == '*') {
					qF.add(i + "," + j + "," + "0");
					map[i][j] = '0';
					cntF++;
				} else if (map[i][j] == '@') {
					qP.add(i + "," + j + "," + "0");
					map[i][j] = '0';
					cntP++;
				}
			}
		}
		int x = 0;
		int y = 0;
		whileend: while (!qF.isEmpty() || !qP.isEmpty()) {
			int cnt = 0;
			if (!qF.isEmpty()) {
				for (int i = 0; i < cntF; i++) {
					String[] val = qF.poll().split(",");
					x = Integer.parseInt(val[0]);
					y = Integer.parseInt(val[1]);
					for (int[] move : movement) {
						int newX = x + move[0];
						int newY = y + move[1];
						if (newX >= 0 && newX < h && newY >= 0 && newY < w) {
							if (map[newX][newY] == '.') {
								qF.add(newX + "," + newY + "," + (Integer.parseInt(val[2]) + 1));
								map[newX][newY] = '0';
								cnt++;
							}
						}
					}
				}
			}
			cntF = cnt;

			cnt = 0;
				if (!qP.isEmpty()) {
					for (int i = 0; i < cntP; i++) {
					String[] val = qP.poll().split(",");
					x = Integer.parseInt(val[0]);
					y = Integer.parseInt(val[1]);
					if (x == 0 || y == 0 || x == h - 1 || y == w - 1) {
						System.out.println(Integer.parseInt(val[2]) + 1);
						return;
					}

					for (int[] move : movement) {
						int newX = x + move[0];
						int newY = y + move[1];
						if (newX >= 0 && newX < h && newY >= 0 && newY < w) {
							if (map[newX][newY] == '.') {
								qP.add(newX + "," + newY + "," + (Integer.parseInt(val[2]) + 1));
								map[newX][newY] = '0';
								cnt++;
							}
						}
					}
				} 
			}else {
				break whileend;
			}
			cntP = cnt;
		}
		System.out.println("IMPOSSIBLE");
	}
}
