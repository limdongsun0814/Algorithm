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
	static int[][] map;
	static int N;	static int M;	static int x;	static int y;
	static HashMap<String, ArrayList<String>> graph;
	static BufferedReader br;
	static ArrayList<int[]> line;
	static ArrayList<String> v;
	static int result;
	public static void main(String[] args) throws Exception {
		br = new BufferedReader(new InputStreamReader(System.in));
		String[] data = br.readLine().split(" ");
		M = Integer.parseInt(data[0]);
		N = Integer.parseInt(data[1]);
		map = new int[N][M];
		make_map();
		find_v();
		bfs();
		System.out.println(has_zero()?-1:result);
	}

	static void make_map() throws IOException {
		for (int i = 0; i < N; i++) {
			String[] data = br.readLine().split(" ");
			for (int j = 0; j < M; j++) {
				map[i][j] = Integer.parseInt(data[j]);
			}
		}
	}

	static void make_line() {
		line = new ArrayList<int[]>();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (i + 1 < N) {
					if (map[i][j] != -1 && map[i + 1][j] != -1) {
						line.add(new int[] { i, j, i + 1, j });
					}
				}

				if (j + 1 < M) {
					if (map[i][j] != -1 && map[i][j + 1] != -1) {
						line.add(new int[] { i, j, i, j + 1 });
					}
				}
			}
		}
	}


	static void find_v() {
		v = new ArrayList<String>();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (map[i][j] == 1) {
					v.add(i + "," + j);
					map[i][j]=1;
				}
			}
		}
	}

	static boolean has_zero() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (map[i][j] == 0) {
					return true;
				}
			}
		}
		return false;
	}
	
	static void bfs() {
		Queue<String> q = new LinkedList<String>();
		Queue<String> buffer = new LinkedList<String>();
		for (String i : v) {
			q.add(i);
			buffer.add(i);
		}
		result=-1; // 자기 자신은 이미 익어서 -1
		while (!buffer.isEmpty()) {
			buffer.clear();
			while (!q.isEmpty()) {
				String val = q.poll();
				y=Integer.parseInt(val.split(",")[0]);
				x=Integer.parseInt(val.split(",")[1]);
				if (y + 1 < N) {
					if ( map[y + 1][x] == 0) {
						buffer.add((y+1)+","+x);
						map[y+1][x]=1;
					}
				}
				if (x + 1 < M) {
					if ( map[y][x + 1] ==0) {
						buffer.add(y+","+(x+1));
						map[y][x+1]=1;
					}
				}
				if (y - 1 >= 0) {
					if (map[y - 1][x] ==0) {
						buffer.add(y-1+","+x);
						map[y-1][x]=1;
					}
				}
				if (x - 1 >= 0) {
					if ( map[y][x - 1] == 0) {
						buffer.add(y+","+(x-1));
						map[y][x-1]=1;
					}
				}
			}
			q.addAll(buffer);
			result++;
		}
	}

	static void print_map() {
		System.out.println("=====print map start=====");
		for (int i = 0; i < N; i++) {
			System.out.println(Arrays.toString(map[i]));
		}
		System.out.println("====print map end======");
	}

	static void print_line() {
		System.out.println("====print line start======");
		for (int[] arr : line) {
			System.out.println(Arrays.toString(arr));
		}
		System.out.println("=====print line end=====" + line.size());
	}

	static void print_graph() {
		System.out.println("====print graph start======"+graph.size());
		for (String arr : graph.keySet()) {
			System.out.println(arr + " : " + graph.get(arr));
		}
		System.out.println("=====print graph end=====" + line.size());
	}

	static void print_v() {
		System.out.println("====print v start======");
		for (String arr : v) {
			System.out.println(arr );
		}
		System.out.println("=====print v end=====" + line.size());
	}
	
	
}

